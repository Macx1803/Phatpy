# Nhập số điện thoại
s = input("Nhập số điện thoại (S): ")

# Tập hợp đầy đủ các chữ số từ '0' đến '9'
all_digits = set("0123456789")

# Tập hợp các chữ số có trong S
present_digits = set(s)

# Những số không xuất hiện (Phép hiệu: all_digits - present_digits)
missing_digits = sorted(list(all_digits - present_digits))

print(f"Các ký số không xuất hiện: {missing_digits}")