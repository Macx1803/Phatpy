from datetime import datetime

S = 'Sep 18 2019 2:43PM'

dinh_dang = "%b %d %Y %I:%M%p"
kieu_ngay = datetime.strptime(S, dinh_dang)
print(f"Chuỗi ban đầu: {S}")
print(f"Kiểu dữ liệu sau khi chuyển: {type(kieu_ngay)}")
print(f"Giá trị đối tượng ngày: {kieu_ngay}")