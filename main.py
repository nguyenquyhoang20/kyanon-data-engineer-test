import pandas as pd
import os

# Đường dẫn tới file CSV
INPUT_PATH = os.path.join("data", "orders.csv")
OUTPUT_PATH = os.path.join("data", "report.csv")

def main():
    # 1. Đọc dữ liệu từ file orders.csv
    df = pd.read_csv(INPUT_PATH)
    print("=== DỮ LIỆN GỐC ===")
    print(df)

    # 2. Lọc các đơn hàng có status = 'completed'
    completed_orders = df[df["status"] == "completed"]

    # 3. Tính tổng amount theo order_date
    report = completed_orders.groupby("order_date")["amount"].sum().reset_index()

    # 4. Đổi tên cột cho đẹp
    report.columns = ["date", "amount"]

    # 5. Xuất ra file report.csv
    report.to_csv(OUTPUT_PATH, index=False)

    print("\n=== KẾT QUẢ BÁO CÁO ===")
    print(report)
    print(f"\nFile báo cáo đã được tạo tại: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

