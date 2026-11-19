"""
===============================================================================
THÀNH VIÊN 4: KỊCH BẢN THỰC NGHIỆM, ĐO KIỂM & VẼ BIỂU ĐỒ (BENCHMARK SUITE)
===============================================================================
Chức năng (Đáp ứng Mục 5.7 & Mục 6.2 trong Đề cương - 3.5/10 điểm):
Thực hiện tự động 04 kịch bản thí nghiệm và xuất bảng số liệu + biểu đồ (.png)
vào thư mục `docs/charts/` và kết quả JSON tại `docs/benchmark_results.json`
để đưa trực tiếp vào Báo cáo cuối kỳ:

- Thí nghiệm 1 (Throughput & Latency): Đo tốc độ tiếp nhận và xử lý vi lô
  (Micro-batch) ở các mức tải 1.000, 5.000, 10.000 và 20.000 bản ghi.
- Thí nghiệm 2 (Storage Compression Efficiency): So sánh dung lượng lưu trữ giữa
  Raw JSON Lines, Raw CSV và Apache Parquet (Snappy) trên tập dữ liệu giao dịch.
- Thí nghiệm 3 (Partition Pruning Speedup): So sánh thời gian truy vấn SQL giữa
  lưu trữ Không phân vùng (Flat) và Có phân vùng (Partitioned `tx_date/tx_type`).
- Thí nghiệm 4 (Veracity & Deduplication Accuracy): Kiểm chứng độ chính xác khi
  bơm dữ liệu hỗn hợp (Hợp lệ + Trùng lặp + Lỗi Schema/Số âm).

Cách chạy:
    ./.venv/bin/python -m src.benchmark.run_benchmarks --records 50000
"""

import argparse
import json
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

import duckdb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from src.config import PROJECT_ROOT
from src.ingestion_sink.spark_kafka_to_lake import validate_transaction
from src.producer.transaction_producer import generate_synthetic_record, inject_fault

CHARTS_DIR = PROJECT_ROOT / "docs" / "charts"
BENCH_TMP_DIR = PROJECT_ROOT / "data" / "benchmark_tmp"
RESULTS_JSON = PROJECT_ROOT / "docs" / "benchmark_results.json"


def generate_dataset(num_records: int) -> list[dict]:
    base_date = datetime.now(timezone.utc)
    records = []
    for i in range(1, num_records + 1):
        rec = generate_synthetic_record(i, base_date)
        rec["tx_date"] = rec["event_time"][:10]
        records.append(rec)
    return records


def experiment_1_throughput_latency(records: list[dict]) -> pd.DataFrame:
    """Thí nghiệm 1: Đo thông lượng tiếp nhận & độ trễ vi lô ở các quy mô tải."""
    batch_sizes = [1000, 5000, 10000, 20000]
    results = []

    print("[EXP 1] Đang đo đạc Throughput & Latency qua các mức tải vi lô...")
    for size in batch_sizes:
        if len(records) < size:
            batch_data = (records * ((size // len(records)) + 1))[:size]
        else:
            batch_data = records[:size]

        # Đo thời gian toàn trình: Validate Schema + Dedup Check + Partition Routing + Parquet In-memory Buffer
        start_time = time.perf_counter()
        seen = set()
        valid_records = []
        quarantine_records = []

        for item in batch_data:
            ok, _ = validate_transaction(item)
            if not ok:
                quarantine_records.append(item)
                continue
            tx_id = item["transaction_id"]
            if tx_id in seen:
                continue
            seen.add(tx_id)
            valid_records.append(item)

        # Chuyển đổi định dạng Parquet Columnar buffer
        if valid_records:
            df_valid = pd.DataFrame(valid_records)
            _ = pa.Table.from_pandas(df_valid, preserve_index=False)

        elapsed = time.perf_counter() - start_time
        latency_ms = round(elapsed * 1000, 2)
        throughput = round(size / elapsed, 1)

        results.append({
            "Batch_Size": f"{size:,} msgs",
            "Records": size,
            "Latency_ms": latency_ms,
            "Throughput_rec_sec": throughput,
        })

    df_res = pd.DataFrame(results)

    # Vẽ biểu đồ 2 đồ thị kết hợp (Throughput bar chart + Latency line chart)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8))

    # Panel 1: Throughput
    bars = ax1.bar(
        df_res["Batch_Size"],
        df_res["Throughput_rec_sec"],
        color=["#3498db", "#2980b9", "#1abc9c", "#16a085"],
        edgecolor="#2c3e50",
        linewidth=1,
    )
    ax1.set_title("Thông lượng Xử lý Ingestion (Throughput)", fontsize=12, fontweight="bold", pad=12)
    ax1.set_ylabel("Thông lượng (bản ghi / giây)", fontsize=10)
    ax1.set_xlabel("Quy mô Mẻ (Micro-batch Size)", fontsize=10)
    ax1.grid(axis="y", linestyle="--", alpha=0.5)
    for bar in bars:
        h = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, h + 200, f"{h:,.0f} r/s", ha="center", va="bottom", fontsize=9, fontweight="bold")

    # Panel 2: Latency
    ax2.plot(
        df_res["Batch_Size"],
        df_res["Latency_ms"],
        marker="o",
        color="#e74c3c",
        linewidth=2.5,
        markersize=8,
        label="Độ trễ xử lý (ms)",
    )
    ax2.set_title("Độ trễ Xử lý theo Kích thước Lô (Latency)", fontsize=12, fontweight="bold", pad=12)
    ax2.set_ylabel("Độ trễ trung bình (ms)", fontsize=10)
    ax2.set_xlabel("Quy mô Mẻ (Micro-batch Size)", fontsize=10)
    ax2.grid(True, linestyle="--", alpha=0.5)
    for idx, row in df_res.iterrows():
        ax2.annotate(
            f"{row['Latency_ms']} ms",
            (row["Batch_Size"], row["Latency_ms"]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontweight="bold",
            color="#c0392b",
        )

    plt.suptitle("Thí nghiệm 1: Đánh giá Hiệu năng Ingestion (Throughput & Latency)", fontsize=14, fontweight="bold", y=1.03)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "exp1_throughput_latency.png", dpi=200, bbox_inches="tight")
    plt.close()
    return df_res


def experiment_2_compression(records: list[dict]) -> pd.DataFrame:
    """Thí nghiệm 2: So sánh dung lượng lưu trữ: CSV vs JSON Lines vs Parquet (Snappy)."""
    BENCH_TMP_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(records)

    csv_path = BENCH_TMP_DIR / "transactions.csv"
    json_path = BENCH_TMP_DIR / "transactions.json"
    parquet_path = BENCH_TMP_DIR / "transactions.snappy.parquet"

    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", lines=True)
    pq.write_table(pa.Table.from_pandas(df, preserve_index=False), parquet_path, compression="snappy")

    json_mb = round(json_path.stat().st_size / (1024 * 1024), 2)
    csv_mb = round(csv_path.stat().st_size / (1024 * 1024), 2)
    parquet_mb = round(parquet_path.stat().st_size / (1024 * 1024), 2)

    results = pd.DataFrame(
        [
            {"Format": "Raw JSON Lines", "Size_MB": json_mb, "Savings_vs_JSON": "0.0%"},
            {
                "Format": "Raw CSV",
                "Size_MB": csv_mb,
                "Savings_vs_JSON": f"{round((1 - csv_mb / json_mb) * 100, 1)}%",
            },
            {
                "Format": "Parquet (Snappy)",
                "Size_MB": parquet_mb,
                "Savings_vs_JSON": f"{round((1 - parquet_mb / json_mb) * 100, 1)}%",
            },
        ]
    )

    plt.figure(figsize=(7.5, 4.8))
    colors = ["#e74c3c", "#f39c12", "#27ae60"]
    bars = plt.bar(results["Format"], results["Size_MB"], color=colors, edgecolor="#2c3e50", linewidth=1)
    plt.title(f"Thí nghiệm 2: Dung lượng lưu trữ trên Data Lake ({len(records):,} giao dịch)", fontsize=13, fontweight="bold", pad=12)
    plt.ylabel("Dung lượng chiếm dụng (MB)", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for idx, bar in enumerate(bars):
        yval = bar.get_height()
        pct = results.iloc[idx]["Savings_vs_JSON"]
        label = f"{yval} MB\n(-{pct})" if idx > 0 else f"{yval} MB\n(Gốc 100%)"
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.15, label, ha="center", va="bottom", fontweight="bold", fontsize=9)

    plt.ylim(0, max(results["Size_MB"]) * 1.25)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "exp2_storage_compression.png", dpi=200, bbox_inches="tight")
    plt.close()
    return results


def experiment_3_partition_pruning(records: list[dict]) -> pd.DataFrame:
    """Thí nghiệm 3: So sánh thời gian truy vấn SQL giữa Không Partition và Có Partition (tx_date/tx_type)."""
    flat_dir = BENCH_TMP_DIR / "flat_parquet"
    part_dir = BENCH_TMP_DIR / "partitioned_parquet"
    if flat_dir.exists():
        shutil.rmtree(flat_dir)
    if part_dir.exists():
        shutil.rmtree(part_dir)
    flat_dir.mkdir(parents=True)
    part_dir.mkdir(parents=True)

    df = pd.DataFrame(records)
    table = pa.Table.from_pandas(df, preserve_index=False)

    # 1. Ghi dạng không phân vùng
    pq.write_table(table, flat_dir / "all_data.snappy.parquet", compression="snappy")

    # 2. Ghi dạng phân vùng chuẩn Hive (tx_date / tx_type)
    pq.write_to_dataset(
        table,
        root_path=str(part_dir),
        partition_cols=["tx_date", "tx_type"],
        compression="snappy",
    )

    target_date = df["tx_date"].iloc[0]
    con = duckdb.connect(":memory:")

    # Đo thời gian quét bảng không phân vùng (10 lần lấy trung bình)
    t0 = time.perf_counter()
    for _ in range(10):
        con.execute(
            f"""
            SELECT COUNT(*), SUM(amount)
            FROM read_parquet('{(flat_dir / "*.parquet").as_posix()}')
            WHERE tx_date = '{target_date}' AND tx_type = 'TRANSFER'
            """
        ).fetchall()
    flat_ms = ((time.perf_counter() - t0) / 10) * 1000

    # Đo thời gian quét bảng có phân vùng (Partition Pruning - 10 lần lấy trung bình)
    t1 = time.perf_counter()
    for _ in range(10):
        con.execute(
            f"""
            SELECT COUNT(*), SUM(amount)
            FROM read_parquet('{(part_dir / "*/*/*.parquet").as_posix()}', hive_partitioning=true)
            WHERE tx_date = '{target_date}' AND tx_type = 'TRANSFER'
            """
        ).fetchall()
    part_ms = ((time.perf_counter() - t1) / 10) * 1000

    speedup = round(flat_ms / part_ms, 2) if part_ms > 0 else 1.0

    results = pd.DataFrame(
        [
            {"Storage_Layout": "Unpartitioned (Quét toàn bộ)", "Query_Time_ms": round(flat_ms, 2), "Speedup": "1.0x (Cơ sở)"},
            {"Storage_Layout": "Partitioned (tx_date/tx_type)", "Query_Time_ms": round(part_ms, 2), "Speedup": f"{speedup}x nhanh hơn"},
        ]
    )

    plt.figure(figsize=(7.5, 4.8))
    bars = plt.bar(results["Storage_Layout"], results["Query_Time_ms"], color=["#7f8c8d", "#2980b9"], edgecolor="#2c3e50", linewidth=1)
    plt.title(f"Thí nghiệm 3: Tốc độ truy vấn SQL Partition Pruning ({len(records):,} bản ghi)", fontsize=13, fontweight="bold", pad=12)
    plt.ylabel("Thời gian thực thi trung bình (ms)", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for idx, bar in enumerate(bars):
        yval = bar.get_height()
        sp = results.iloc[idx]["Speedup"]
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f"{yval} ms\n({sp})", ha="center", va="bottom", fontweight="bold", fontsize=9)

    plt.ylim(0, max(results["Query_Time_ms"]) * 1.3)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "exp3_partition_pruning.png", dpi=200, bbox_inches="tight")
    plt.close()
    return results


def experiment_4_veracity_deduplication(records: list[dict]) -> pd.DataFrame:
    """Thí nghiệm 4: Kiểm thử độ chính xác lọc lỗi (Quarantine) và khử trùng lặp (Deduplication)."""
    valid_base = records[:10000]
    duplicates = valid_base[:500]  # 500 bản ghi trùng lặp
    corrupted = [inject_fault(r) for r in valid_base[500:1000]]  # 500 bản ghi lỗi

    stream_input = valid_base + duplicates + corrupted
    seen_ids = set()
    accepted = 0
    deduped = 0
    quarantined = 0

    for item in stream_input:
        ok, _ = validate_transaction(item)
        if not ok:
            quarantined += 1
            continue
        tx_id = item["transaction_id"]
        if tx_id in seen_ids:
            deduped += 1
            continue
        seen_ids.add(tx_id)
        accepted += 1

    results = pd.DataFrame(
        [
            {"Category": "Tổng đầu vào (Input)", "Records": len(stream_input), "Percentage": "100.0%"},
            {"Category": "Lưu hợp lệ (Bronze Lake)", "Records": accepted, "Percentage": f"{accepted / len(stream_input) * 100:.1f}%"},
            {"Category": "Khử trùng lặp (Deduplicated)", "Records": deduped, "Percentage": f"{deduped / len(stream_input) * 100:.1f}%"},
            {"Category": "Cách ly lỗi (Quarantine/DLQ)", "Records": quarantined, "Percentage": f"{quarantined / len(stream_input) * 100:.1f}%"},
        ]
    )

    plt.figure(figsize=(8.5, 4.8))
    bars = plt.bar(
        results["Category"],
        results["Records"],
        color=["#34495e", "#27ae60", "#f39c12", "#c0392b"],
        edgecolor="#2c3e50",
        linewidth=1,
    )
    plt.title("Thí nghiệm 4: Tính toàn vẹn dữ liệu (Veracity & Deduplication Accuracy)", fontsize=13, fontweight="bold", pad=12)
    plt.ylabel("Số lượng bản ghi", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for idx, bar in enumerate(bars):
        yval = bar.get_height()
        pct = results.iloc[idx]["Percentage"]
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 150, f"{yval:,}\n({pct})", ha="center", va="bottom", fontweight="bold", fontsize=9)

    plt.ylim(0, max(results["Records"]) * 1.22)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "exp4_veracity_accuracy.png", dpi=200, bbox_inches="tight")
    plt.close()
    return results


def main():
    parser = argparse.ArgumentParser(description="Chạy bộ thực nghiệm Benchmark cho Báo cáo (Thành viên 4)")
    parser.add_argument("--records", type=int, default=50000, help="Số lượng bản ghi thử nghiệm")
    args = parser.parse_args()

    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n===============================================================================")
    print(f"BẮT ĐẦU CHẠY BỘ THỰC NGHIỆM ĐO KIỂM BENCHMARK ({args.records:,} BẢN GHI)")
    print(f"===============================================================================\n")

    t_start = time.perf_counter()
    print(f"[BENCHMARK] Đang sinh {args.records:,} bản ghi giao dịch tài chính chuẩn PaySim...")
    records = generate_dataset(args.records)

    print("\n--- KẾT QUẢ THÍ NGHIỆM 1: THÔNG LƯỢNG & ĐỘ TRỄ TIẾP NHẬN (THROUGHPUT & LATENCY) ---")
    df_tp = experiment_1_throughput_latency(records)
    print(df_tp.to_string(index=False))

    print("\n--- KẾT QUẢ THÍ NGHIỆM 2: HIỆU QUẢ NÉN LƯU TRỮ (STORAGE COMPRESSION) ---")
    df_comp = experiment_2_compression(records)
    print(df_comp.to_string(index=False))

    print("\n--- KẾT QUẢ THÍ NGHIỆM 3: TỐC ĐỘ TRUY VẤN PARTITION PRUNING (SQL ACCELERATION) ---")
    df_part = experiment_3_partition_pruning(records)
    print(df_part.to_string(index=False))

    print("\n--- KẾT QUẢ THÍ NGHIỆM 4: ĐỘ CHÍNH XÁC VERACITY & KHỬ TRÙNG LẶP ---")
    df_ver = experiment_4_veracity_deduplication(records)
    print(df_ver.to_string(index=False))

    # Dọn thư mục tạm
    if BENCH_TMP_DIR.exists():
        shutil.rmtree(BENCH_TMP_DIR)

    # Lưu kết quả tổng hợp vào docs/benchmark_results.json
    total_time = round(time.perf_counter() - t_start, 2)
    summary_data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_benchmark_records": args.records,
        "execution_time_seconds": total_time,
        "experiment_1_throughput_latency": df_tp.to_dict(orient="records"),
        "experiment_2_storage_compression": df_comp.to_dict(orient="records"),
        "experiment_3_partition_pruning": df_part.to_dict(orient="records"),
        "experiment_4_veracity_accuracy": df_ver.to_dict(orient="records"),
    }
    with open(RESULTS_JSON, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)

    print(f"\n===============================================================================")
    print(f"[BENCHMARK HOÀN TẤT] Thời gian thực thi: {total_time} giây.")
    print(f"- Toàn bộ 04 biểu đồ đã được xuất tại: {CHARTS_DIR}")
    print(f"- Bảng dữ liệu JSON tổng hợp đã lưu tại: {RESULTS_JSON}")
    print(f"===============================================================================\n")


if __name__ == "__main__":
    main()
