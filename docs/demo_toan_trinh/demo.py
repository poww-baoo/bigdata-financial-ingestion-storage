import io,json,os,random,sys,time
from pathlib import Path
os.environ.update(KAFKA_BOOTSTRAP_SERVERS='localhost:19092',KAFKA_TOPIC_TRANSACTIONS='financial_demo_2026',KAFKA_TOPIC_DLQ='financial_demo_dlq_2026',MINIO_ENDPOINT='localhost:19000',MINIO_ACCESS_KEY='demo_minio_admin',MINIO_SECRET_KEY='demo_minio_pass_2026',MINIO_BUCKET_NAME='financial-demo-isolated')
from confluent_kafka.admin import AdminClient,NewTopic
from confluent_kafka import Consumer,TopicPartition
from minio import Minio
import pyarrow.parquet as pq
from src.producer.transaction_producer import run_producer
from src.ingestion_sink.spark_kafka_to_lake import run_microbatch_engine
admin=AdminClient({'bootstrap.servers':'localhost:19092'})
for name,fut in admin.create_topics([NewTopic('financial_demo_2026',num_partitions=3,replication_factor=1),NewTopic('financial_demo_dlq_2026',num_partitions=1,replication_factor=1)]).items():fut.result(30);print('Topic created:',name,flush=True)
random.seed(20261112)
producer=run_producer(count=3000,rate=1000,fault_rate=.03,dup_rate=.02)
sink=run_microbatch_engine(batch_size=1000,batch_timeout_sec=2,max_empty_batches=2,consumer_group='demo-20261112')
m=Minio('localhost:19000',access_key='demo_minio_admin',secret_key='demo_minio_pass_2026',secure=False)
def scan(prefix):
 objects=list(m.list_objects('financial-demo-isolated',prefix=prefix,recursive=True)); rows=[]
 for obj in objects:
  if obj.object_name.endswith('.parquet'):
   resp=m.get_object('financial-demo-isolated',obj.object_name)
   try: rows.extend(pq.ParquetFile(io.BytesIO(resp.read())).read().to_pylist())
   finally:resp.close();resp.release_conn()
 return objects,rows
bo,br=scan('bronze/transactions/');qo,qr=scan('quarantine/bad_transactions/')
c=Consumer({'bootstrap.servers':'localhost:19092','group.id':'evidence-observer-2026','enable.auto.commit':False})
try: dlq_high=c.get_watermark_offsets(TopicPartition('financial_demo_dlq_2026',0),timeout=10)[1]
finally:c.close()
ids=[r['transaction_id'] for r in br]
result={'producer':producer,'sink':sink,'bronze_rows':len(br),'bronze_unique_ids':len(set(ids)),'quarantine_rows':len(qr),'dlq_messages':dlq_high,'bronze_files':len(bo),'quarantine_files':len(qo),'bronze_objects':[o.object_name for o in bo],'quarantine_objects':[o.object_name for o in qo]}
checks={'input_equals_received':producer['total_sent']==sink['total_consumed'],'accepted_matches':producer['valid_sent']==len(br)==sink['valid_written'],'duplicates_match':producer['duplicates_sent']==sink['duplicates_dropped'],'faults_match':producer['fault_injected']==len(qr)==sink['quarantined_written']==dlq_high,'bronze_unique':len(ids)==len(set(ids))}
result['checks']=checks
print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
Path('docs/demo_toan_trinh_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
sys.exit(0 if all(checks.values()) else 1)
