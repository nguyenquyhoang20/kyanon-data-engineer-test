# Kyanon Digital - Data Engineer Intern Test (Data Aggregation)

## Mô tả bài tập
Bài tập này được thực hiện trong khuôn khổ chương trình tuyển dụng thực tập sinh Data Engineer tại Kyanon Digital.  
Mục tiêu là xây dựng một quy trình xử lý dữ liệu (data aggregation) bằng ngôn ngữ Python, trong đó:
- Đọc dữ liệu đơn hàng từ file `orders.csv`
- Lọc các đơn hàng có trạng thái `completed`
- Tính tổng doanh thu (`amount`) theo từng ngày (`order_date`)
- Xuất kết quả ra file `report.csv` để phục vụ cho việc phân tích doanh thu

Bài tập mô phỏng một phần nhỏ trong quy trình **ETL (Extract – Transform – Load)** trong thực tế của một hệ thống thương mại điện tử.


---

## ⚙Cách chạy chương trình

### 1Cài đặt thư viện cần thiết
Trước khi chạy, đảm bảo bạn đã cài đặt Python (phiên bản >= 3.8) và thư viện Pandas:
```bash
pip install pandas
2 Chạy chương trình

Di chuyển đến thư mục chứa mã nguồn:
python main.py

3 Kết quả đầu ra

Sau khi chạy xong, chương trình sẽ tạo file report.csv trong thư mục data/
với nội dung tương tự như sau:

date,amount
2025-09-01,250
2025-09-02,100



