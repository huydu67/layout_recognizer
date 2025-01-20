import fitz  # PyMuPDF
import json

# Đường dẫn file
pdf_path = "/home/du/ragflow/deepdoc/vision/input/test_pdf.pdf"  # Đường dẫn file PDF đầu vào
json_path = "/home/du/ragflow/deepdoc/vision/output/page_1.json"  # Đường dẫn file JSON đầu vào
output_pdf_path = "test_pdf_annotated.pdf"  # Đường dẫn file PDF đầu ra

# Đọc dữ liệu JSON
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Mở file PDF
doc = fitz.open(pdf_path)

# Lấy số trang
page_number = data.get("page_number", 1) - 1

if page_number < len(doc):
    page = doc[page_number]

    for item in data.get("content", []):
        x0, top, x1, bottom = item["x0"], item["top"], item["x1"], item["bottom"]
        label = item["label"]
        score = item["score"]

        # Vẽ bounding box lên trang PDF
        rect = fitz.Rect(x0, top, x1, bottom)
        page.draw_rect(rect, color=(1, 0, 0), width=2)
        page.insert_text((x0, top - 10), f"{label} ({score:.2f})", fontsize=10, color=(1, 0, 0))

# Lưu file PDF đã vẽ bounding box
doc.save(output_pdf_path)
print(f"Annotated PDF saved as {output_pdf_path}")