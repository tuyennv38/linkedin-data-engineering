"""
Tiện ích tự động render sơ đồ Mermaid sang ảnh PNG / JPG chất lượng cao cho LinkedIn.
LinkedIn không hỗ trợ định dạng .svg nên script này chuyển đổi toàn bộ sang PNG/JPG.
"""

import sys
import base64
import requests
from pathlib import Path

# Đảm bảo UTF-8 trên Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def render_mmd_file(mmd_path: Path) -> bool:
    if not mmd_path.exists():
        print(f"[!] Không tìm thấy file: {mmd_path}")
        return False

    code = mmd_path.read_text(encoding="utf-8").strip()
    b64_str = base64.urlsafe_b64encode(code.encode("utf-8")).decode("ascii")

    # URL render ảnh chất lượng cao cho LinkedIn
    url_png = f"https://mermaid.ink/img/{b64_str}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AI-DataEng-Agent/1.0"
    }

    try:
        res = requests.get(url_png, headers=headers, timeout=30)
        if res.status_code == 200 and len(res.content) > 500:
            png_path = mmd_path.with_suffix(".png")
            jpg_path = mmd_path.with_suffix(".jpg")

            # Lưu PNG
            png_path.write_bytes(res.content)
            # Lưu đồng thời JPG để bạn có lựa chọn
            jpg_path.write_bytes(res.content)

            print(f"[✔] Đã tạo thành công ảnh PNG/JPG cho LinkedIn:")
            print(f"    - PNG: {png_path} ({len(res.content) // 1024} KB)")
            return True
        else:
            print(f"[!] Lỗi khi gọi mermaid.ink API ({res.status_code}): {res.text[:100]}")
    except Exception as e:
        print(f"[!] Ngoại lệ khi tải ảnh: {e}")

    return False


def render_all():
    diagrams_dir = Path("content/diagrams")
    if not diagrams_dir.exists():
        print("[!] Không tìm thấy thư mục content/diagrams")
        return

    mmd_files = list(diagrams_dir.glob("*.mmd"))
    print(f"[*] Tìm thấy {len(mmd_files)} file .mmd. Bắt đầu xuất ảnh PNG cho LinkedIn...")

    for f in mmd_files:
        render_mmd_file(f)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        render_mmd_file(target)
    else:
        render_all()
