# ⚡ ClickHouse Mastery: LinkedIn Content Production Agent System

Hệ thống AI Multi-Agent chuyên sâu 100% vào **ClickHouse Database**, tự động sản xuất bài viết kỹ thuật chất lượng cao mỗi ngày cho LinkedIn theo lộ trình sư phạm bài bản từ cơ bản đến phức tạp, tập trung giải quyết các bài toán dữ liệu lớn thực tế.

---

## 🗺️ Lộ trình đào tạo tổng thể (Curriculum Roadmap)

Toàn bộ hệ thống vận hành bám sát file lộ trình **`content/clickhouse_roadmap.md`** gồm **8 Module** và **18+ bài toán thực chiến**:

1. **Module 1**: Bản chất kiến trúc Columnar Storage, Vectorized SIMD execution (Tại sao nhanh hơn PostgreSQL 100 lần?).
2. **Module 2**: Bậc thầy họ động cơ MergeTree (`ReplacingMergeTree`, `CollapsingMergeTree`, `AggregatingMergeTree`...).
3. **Module 3**: Tối ưu Sparse Primary Index, Index Granularity (8192) & Data Skipping Indexes (Bloom Filters, MinMax).
4. **Module 4**: Streaming Ingestion tốc độ cao (`Kafka Engine` + `Materialized View`, chữa bệnh "Too many parts").
5. **Module 5**: Tối ưu truy vấn nâng cao: Zero-latency JOINs với `Dictionaries`, `Projections`, `ASOF JOIN`.
6. **Module 6**: **Các bài toán thực tế ClickHouse thống trị**:
   - Thay thế Elasticsearch/ELK stack cho Log & Traces Analytics (chi phí rẻ hơn 80%).
   - Phân tích phễu hành vi người dùng (User Funnel Analysis) với `windowFunnel()`.
   - Giám sát cảm biến IoT & Time-series quy mô hàng trăm triệu metrics/giây.
   - Phát hiện gian lận giao dịch tài chính (Real-time Fraud Detection).
7. **Module 7**: Cụm phân tán Sharding & Replication với `ClickHouse Keeper` (thay thế ZooKeeper).
8. **Module 8**: Tối ưu chi phí sản xuất: Tiered Storage trên AWS S3 / MinIO với Zero-copy replication.

---

## 👥 Đội ngũ 6 Sub-Agents Chuyên gia ClickHouse + 1 Orchestrator

| Sub-Agent | Role Prompt | Nhiệm vụ chính |
| :--- | :--- | :--- |
| 🎯 **content-orchestrator** | `.cursor/agents/content-orchestrator.md` | Nhạc trưởng điều phối pipeline bám sát lộ trình `clickhouse_roadmap.md` |
| 📋 **topic-planner** | `.cursor/agents/topic-planner.md` | Quản lý lộ trình bài học, chọn bài tiếp theo theo thứ tự sư phạm, xác định bài toán thực tế |
| 🔬 **data-researcher** | `.cursor/agents/data-researcher.md` | Nghiên cứu cơ chế nội tại ClickHouse, docs chính thức, kiểm chứng DDL/SQL và benchmarks |
| ✍️ **technical-writer** | `.cursor/agents/technical-writer.md` | Viết bài LinkedIn tiếng Việt chuyên sâu, viral hook, code DDL/SQL thực chiến và visual brief |
| 🛡️ **technical-reviewer** | `.cursor/agents/technical-reviewer.md` | Principal Architect review độc lập (PASS/FAIL): Engine, ORDER BY, partition pruning, anti-patterns |
| 📊 **diagram-designer** | `.cursor/agents/diagram-designer.md` | Vẽ sơ đồ Mermaid (.mmd/SVG) trực quan hóa cấu trúc lưu trữ đĩa, data parts, luồng ingestion |
| 🎨 **visual-designer** | `.cursor/agents/visual-designer.md` | Soạn concept và prompt AI tạo ảnh bìa 3D Isometric chuẩn phong cách nhận diện ClickHouse |

---

## 🚀 Cách sử dụng trong Cursor Chat

Chỉ cần gõ:
```text
/content-orchestrator Hãy sản xuất bài viết ClickHouse tiếp theo theo đúng lộ trình
```
Hệ thống sẽ:
1. Tự động đọc `content/clickhouse_roadmap.md` xem bài nào chưa viết theo thứ tự.
2. Điều phối các sub-agent nghiên cứu, viết, review, vẽ sơ đồ và prompt ảnh bìa.
3. Đánh dấu trạng thái ✅ vào bảng lộ trình.
4. Xuất kết quả đầy đủ vào thư mục `content/`.
