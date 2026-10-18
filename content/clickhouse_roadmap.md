# 🗺️ LỘ TRÌNH TỔNG THỂ: LÀM CHỦ CLICKHOUSE DATABASE TỪ CƠ BẢN ĐẾN CHUYÊN GIA
*(ClickHouse Mastery Series: From Fundamentals to Production Engineering)*

Mục tiêu: Cung cấp chuỗi bài viết kỹ thuật hàng ngày trên LinkedIn, được thiết kế có hệ thống từ trực quan dễ hiểu đến chuyên sâu thực chiến, giải quyết các bài toán "triệu/tỷ bản ghi" mà ClickHouse làm xuất sắc nhất.

---

## 📌 BẢNG THEO DÕI TIẾN ĐỘ BÀI VIẾT

| Bài # | Mã bài | Tên chủ đề | Bài toán thực tế giải quyết | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **01** | `CH-MOD1-01` | **Tại sao ClickHouse nhanh hơn PostgreSQL 100 lần trong Analytics?** | Mổ xẻ Column-Oriented vs Row-Oriented, Vectorized Execution & SIMD | ✅ Đã viết (20/10) |
| **02** | `CH-MOD1-02` | **MergeTree Engine: Trái tim của ClickHouse hoạt động thế nào?** | Cơ chế Immutable Parts, LSM-tree inspired, và quá trình Background Compaction | ✅ Đã viết (21/10) |
| **03** | `CH-MOD1-03` | **Primary Key vs ORDER BY trong ClickHouse: Sai lầm phổ biến của dân RDBMS** | Giải bài toán Sparse Primary Index, Index Granularity (8192) & Data Skipping | ✅ Đã viết (22/10) |
| **04** | `CH-MOD2-01` | **ReplacingMergeTree: Bản chất thật sự của Upsert và Cái bẫy của SELECT FINAL** | Xử lý Duplicate CDC events mà không làm sập CPU/RAM khi truy vấn | ✅ Đã viết (18/10) |
| **05** | `CH-MOD2-02` | **CollapsingMergeTree & VersionedCollapsingMergeTree: Xóa và Cập nhật siêu tốc** | Bài toán Update/Delete trạng thái tài khoản, đơn hàng theo thời gian thực | ⏳ Kế tiếp |
| **06** | `CH-MOD2-03` | **SummingMergeTree vs AggregatingMergeTree: Pre-aggregating tỷ dòng trong nháy mắt** | Báo cáo tài chính, Metrics đếm tiền, lượt clicks mà không cần scan raw data | ⏳ Chờ |
| **07** | `CH-MOD3-01` | **Tối ưu Partitioning & Data Skipping Indexes (Bloom Filters, MinMax, Set)** | Bài toán lọc dữ liệu chuỗi (String search, UUID, IP) triệu dòng dưới 10ms | ⏳ Chờ |
| **08** | `CH-MOD4-01` | **Realtime Ingestion: Kafka Engine kết hợp Materialized View** | Xây dựng Pipeline Ingestion tự động hóa từ Kafka vào ClickHouse không cần app trung gian | ⏳ Chờ |
| **09** | `CH-MOD4-02` | **Chữa bệnh "Too many parts in all data parts in table": Nghệ thuật Batching Ingestion** | Khắc phục lỗi crash phổ biến nhất khi streaming dữ liệu vào ClickHouse | ⏳ Chờ |
| **10** | `CH-MOD5-01` | **Sức mạnh vô địch của Dictionaries trong ClickHouse: Zero-latency Joins** | Giải quyết bài toán JOIN dimension tables hàng triệu dòng mà không tốn bộ nhớ | ⏳ Chờ |
| **11** | `CH-MOD5-02` | **Projections trong ClickHouse: 1 Bảng nhưng Nhiều kiểu ORDER BY vật lý** | Tối ưu hóa đa dạng câu truy vấn khác nhau mà không cần tạo nhiều bảng trùng lặp | ⏳ Chờ |
| **12** | `CH-MOD6-01` | **Bài toán 1: Log & Traces Analytics - Thay thế hoàn toàn Elasticsearch/ELK stack** | Lưu trữ Petabytes log hệ thống, nén 1:10, query regex và full-text siêu rẻ | ⏳ Chờ |
| **13** | `CH-MOD6-02` | **Bài toán 2: Phân tích Hành vi Người dùng & Phễu chuyển đổi (Funnel Analysis)** | Tận dụng windowFunnel(), sequenceMatch() để vẽ User Journey hàng tỷ click | ⏳ Chờ |
| **14** | `CH-MOD6-03` | **Bài toán 3: Giám sát IoT & Time-series Metrics quy mô triệu thiết bị** | Lưu trữ cảm biến sensor, resampling dữ liệu với toStartOfFiveMinutes(), ASOF JOIN | ⏳ Chờ |
| **15** | `CH-MOD6-04` | **Bài toán 4: Phát hiện Gian lận Thời gian thực (Real-time Fraud & Anomaly Detection)** | Phát hiện giao dịch bất thường trong vài mili-giây với Sliding Windows | ⏳ Chờ |
| **16** | `CH-MOD7-01` | **Distributed Table Engine & Kiến trúc Sharding/Replication trong ClickHouse** | Two-phase distributed query, Scatter-Gather pattern và cách chia shard key | ⏳ Chờ |
| **17** | `CH-MOD7-02` | **ClickHouse Keeper thay thế Apache ZooKeeper: Thiết lập High Availability đơn giản** | Quản lý metadata phân tán, tránh bottleneck ZooKeeper trong production | ⏳ Chờ |
| **18** | `CH-MOD8-01` | **ClickHouse trên S3/Object Storage & Zero-copy Replication: Giảm 80% chi phí lưu trữ** | Tách biệt Compute và Storage (Disaggregated Storage) cho dữ liệu Cold | ⏳ Chờ |

---

## 🎯 8 MODULE KIẾN THỨC CỐT LÕI

### Module 1: Bản chất & Tinh hoa Kiến trúc ClickHouse (Cơ bản)
* Hiểu sâu kiến trúc Columnar Storage, Vectorized Execution, SIMD instructions.
* Cơ chế nén dữ liệu (LZ4, ZSTD, Delta, T64, DoubleDelta, Gorilla).
* Vòng đời của một Block dữ liệu từ khi Insert đến khi ghi xuống Disk.

### Module 2: Bậc thầy các Table Engines họ MergeTree
* **MergeTree**: Động cơ cơ bản, immutable parts, merge algorithm.
* **ReplacingMergeTree**: Khử trùng lặp, versioning, giải mã SELECT FINAL vs argMax.
* **CollapsingMergeTree & VersionedCollapsingMergeTree**: Sign (+1/-1), xóa/cập nhật dữ liệu CDC không khóa bảng.
* **SummingMergeTree & AggregatingMergeTree**: Pre-aggregating data states, AggregateFunction/SimpleAggregateFunction.

### Module 3: Kỹ thuật Đánh Index & Partitioning
* Tư duy chọn `ORDER BY` vs `PRIMARY KEY` (Primary key là tiền tố của Order by).
* Cơ chế Sparse Index (chỉ lưu 1 index mark mỗi 8192 dòng) - Sự khác biệt với B-Tree của PostgreSQL.
* Data Skipping Indexes: MinMax, Set, Bloom Filter, TokenBF.
* Partition Pruning và chiến lược phân vùng (`toYYYYMM`, `toDate`).

### Module 4: Streaming Ingestion & Realtime Pipelines
* Kiến trúc tích hợp Apache Kafka trực tiếp bằng `Kafka Engine` + `Materialized View`.
* Xử lý lỗi kinh điển: "Too many parts (100+) in all data parts in table".
* Tư duy Ingestion Batching: Buffer Table, Async Insert, In-memory blocks.

### Module 5: Tối ưu hóa Nâng cao & Bí quyết Truy vấn
* **Dictionaries**: In-memory, Redis, PostgreSQL cache để JOIN tốc độ ánh sáng.
* **Projections**: Lưu trữ nhiều sắp xếp vật lý trong 1 bảng, tự động routing query.
* Phép toán **ASOF JOIN** cho Time-series và tài chính (nối bản ghi gần nhất theo thời gian).
* Array & Nested Types: Xử lý dữ liệu bán cấu trúc (Semi-structured JSON) với hiệu năng cột thuần túy.

### Module 6: Các Bài toán Thực tế ClickHouse Thống trị
* **Log & Trace Analytics**: Thay thế Elasticsearch/Loki với chi phí chỉ bằng 1/5.
* **Product & Web Analytics**: Xây dựng Google Analytics nội bộ với `windowFunnel()`, `retention()`.
* **IoT & Telemetry Monitoring**: Hàng trăm triệu metrics/giây, downsampling dữ liệu cũ.
* **Fraud & Financial Analytics**: Phân tích giao dịch thẻ, phát hiện mẫu hình gian lận trong thời gian thực.

### Module 7: Scale, Sharding & Phân tán
* Thiết kế cụm Cluster: `Distributed` Engine, Shards, Replicas.
* Điều phối Cluster với ClickHouse Keeper (Native C++ thay ZooKeeper).
* Chiến lược Shard Key: Hash sharding, Random sharding, và cách tránh Distributed JOIN bottleneck.

### Module 8: Production Operations & Cost Optimization
* Kiến trúc Tiered Storage: Hot data trên NVMe SSD, Warm/Cold data tự đẩy lên AWS S3 / MinIO.
* Zero-copy replication trên Object Storage.
* Monitor hiệu năng qua các bảng hệ thống: `system.query_log`, `system.parts`, `system.merges`.
