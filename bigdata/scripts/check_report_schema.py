"""Record current validator behavior without importing or starting the pipeline.

Run from the repository root: python3 scripts/check_report_schema.py
This probe documents limitations; accepted inputs are not proof of schema compliance.
"""
import ast
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source_path = ROOT / "src/ingestion_sink/spark_kafka_to_lake.py"
config_path = ROOT / "src/config.py"
source = source_path.read_text(encoding="utf-8")
config = ast.parse(config_path.read_text(encoding="utf-8"))
types = next(ast.literal_eval(node.value) for node in config.body
             if isinstance(node, ast.Assign)
             and any(isinstance(t, ast.Name) and t.id == "VALID_TX_TYPES" for t in node.targets))
function = next(node for node in ast.parse(source).body
                if isinstance(node, ast.FunctionDef) and node.name == "validate_transaction")
namespace = {"VALID_TX_TYPES": types}
exec(compile(ast.Module(body=[function], type_ignores=[]), str(source_path), "exec"), namespace)
base = dict(transaction_id="PROBE-001", event_time="2026-11-12T08:00:00Z", step=1,
            tx_type="PAYMENT", amount=100.0, currency="VND", sender_id="C01",
            sender_old_balance=1000.0, sender_new_balance=900.0,
            receiver_id="M01", payment_channel="MOBILE_APP", is_fraud_label=0)
cases = [
    ("valid_baseline", {}, [], True),
    ("amount_not_numeric", {"amount": "abc"}, [], False),
    ("amount_numeric_string", {"amount": "100"}, [], True),
    ("missing_sender_id", {}, ["sender_id"], False),
    ("missing_event_time", {}, ["event_time"], True),
    ("invalid_event_time", {"event_time": "not-a-date"}, [], True),
    ("invalid_step", {"step": "abc"}, [], True),
    ("unknown_currency", {"currency": "XYZ"}, [], True),
    ("python_nan_amount", {"amount": float("nan")}, [], True),
]
results = []
for name, update, remove, expected in cases:
    record = copy.deepcopy(base)
    record.update(update)
    for key in remove:
        record.pop(key)
    accepted, reason = namespace["validate_transaction"](record)
    safe_record = {k: ("Python float NaN (not a JSON payload)" if isinstance(v, float) and v != v else v)
                   for k, v in record.items()}
    results.append(dict(case=name, input=safe_record, accepted=accepted, reason=reason,
                        matches_documented_behavior=accepted == expected))
output = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
              source="src/ingestion_sink/spark_kafka_to_lake.py",
              source_sha256=hashlib.sha256(source.encode()).hexdigest(),
              method="AST extraction of validate_transaction and literal VALID_TX_TYPES; no service imports",
              scope="Isolated Python function only; no Kafka, Arrow serialization or MinIO; not a compliance test",
              cases=results, all_match_documented_behavior=all(r["matches_documented_behavior"] for r in results))
destination = ROOT / "docs/schema_validation_probe.json"
destination.write_text(json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
print(f"Recorded {len(results)} cases; documented behavior matches: {output['all_match_documented_behavior']}")
print(destination)
