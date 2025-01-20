DeepDoc - Trích Xuất Bố Cục Tài Liệu Tự Động
Giới Thiệu

DeepDoc là một hệ thống nhận diện bố cục tài liệu sử dụng công nghệ OCR kết hợp với các mô hình học sâu để trích xuất các thành phần như tiêu đề, nội dung văn bản, bảng biểu, hình ảnh minh họa, từ tài liệu PDF và hình ảnh.
Dự án giúp tự động hóa quá trình phân tích tài liệu, hỗ trợ trong việc số hóa và tìm kiếm thông tin hiệu quả.
Cấu Trúc Thư Mục

ragflow/
├── deepdoc/
│   ├── vision/
│   │   ├── input/               # Thư mục chứa các tài liệu PDF đầu vào
│   │   ├── output/              # Thư mục chứa kết quả JSON đầu ra
│   │   ├── bbox.py              # Script vẽ bounding boxes lên PDF
│   │   ├── layout_recognizer.py  # Mô-đun nhận diện bố cục
│   │   ├── t_recognizer.py       # Mô-đun nhận diện bảng và văn bản
│   │   ├── configs/              # Thư mục chứa các file cấu hình
│   │   ├── utils/                 # Các tiện ích xử lý hình ảnh và file
│   ├── docs/                     # Tài liệu liên quan
│   ├── README.md                  # Hướng dẫn sử dụng dự án

Hướng Dẫn Cài Đặt
Yêu Cầu Hệ Thống

    Python 3.8 trở lên
    Các thư viện cần thiết:

Cài Đặt Môi Trường

    Tạo môi trường ảo (tùy chọn):

python3 -m venv venv
source venv/bin/activate  # Trên Linux/macOS
venv\\Scripts\\activate   # Trên Windows

Cài đặt các thư viện phụ thuộc:

    pip install -r requirements.txt

Hướng Dẫn Sử Dụng
Bước 1: Chuẩn Bị Tài Liệu

    Đặt file PDF cần xử lý vào thư mục deepdoc/vision/input/.

Bước 2: Chạy Trích Xuất Bố Cục

Chạy lệnh sau để trích xuất bố cục từ tài liệu PDF:

python deepdoc/vision/t_recognizer.py --inputs deepdoc/vision/input --output_dir deepdoc/vision/output --mode layout --threshold 0.5

Tham số lệnh:

    --inputs: Thư mục chứa file PDF đầu vào.
    --output_dir: Thư mục lưu file JSON đầu ra.
    --mode: Chế độ nhận diện (layout hoặc tsr).
    --threshold: Ngưỡng điểm tin cậy để lọc kết quả.

Sau khi chạy, kết quả sẽ được lưu trong thư mục deepdoc/vision/output/ dưới dạng file JSON.
Bước 3: Vẽ Bounding Boxes lên PDF

Để vẽ kết quả nhận diện lên tài liệu PDF, chạy lệnh sau:

python deepdoc/vision/bbox.py

Kết quả:

    File PDF có bounding boxes sẽ được lưu trong thư mục deepdoc/vision/output_annotated/.

Cấu Trúc File JSON Đầu Ra

Ví dụ về nội dung file page_1.json:

{
    "page_number": 1,
    "content": [
        {
            "label": "title",
            "x0": 83.82,
            "top": 276.60,
            "x1": 414.36,
            "bottom": 291.82,
            "score": 0.61
        },
        {
            "label": "table",
            "x0": 84.09,
            "top": 114.15,
            "x1": 539.90,
            "bottom": 256.76,
            "score": 0.96
        }
    ]
}

Ý nghĩa các trường trong JSON:

    page_number: Số trang được xử lý.
    label: Nhãn vùng nhận diện (title, text, table, etc.).
    x0, top, x1, bottom: Tọa độ của bounding box.
    score: Điểm số độ tin cậy của vùng nhận diện.

Giải Quyết Vấn Đề Thường Gặp

    Bounding boxes không hiển thị đúng vị trí trên PDF
        Kiểm tra kích thước của file PDF đầu vào.
        Điều chỉnh tọa độ bằng cách thêm tỷ lệ thu phóng khi vẽ bounding boxes.

    Không có dữ liệu JSON đầu ra
        Kiểm tra xem file PDF có nội dung hợp lệ không.
        Giảm giá trị --threshold để lấy nhiều kết quả hơn.

    Lỗi thiếu thư viện
        Chạy lệnh sau để cài đặt thư viện còn thiếu:

        pip install pymupdf numpy argparse

Kế Hoạch Cải Tiến

    Tăng độ chính xác mô hình:
    Nghiên cứu và áp dụng các phương pháp xử lý trước hình ảnh để cải thiện kết quả.

    Bổ sung khả năng nhận diện bảng phức tạp:
    Tích hợp thêm mô hình nhận diện bảng như PaddleOCR hoặc TableNet.

    Tối ưu hóa hiệu suất:
    Giảm thời gian xử lý bằng cách sử dụng GPU và tối ưu hóa thuật toán phân tích.

