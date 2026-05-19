def helper(n, max_len, is_extended=False):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"]

    # Đệ quy lấy tầng bên trong
    sub_list = helper(n - 2, max_len, is_extended)
    result = []

    for s in sub_list:
        if n != max_len:
            result.append("0" + s + "0")
        
        result.append("1" + s + "1")
        result.append("8" + s + "8")
        result.append("6" + s + "9")
        result.append("9" + s + "6")
        
        if is_extended:
            result.append("2" + s + "5")
            result.append("5" + s + "2")

    return result

def generate_strobogrammatic(n, is_extended=False):
    result = helper(n, n, is_extended)
    
    result.sort()
    return result

def output_format(lst, label):
    print(f"\n--- {label} (Tổng cộng: {len(lst)} số) ---")
    if not lst:
        print("Không có số nào thỏa mãn.")
        return
        
    for index, num in enumerate(lst, 1):
        print(f"{num:<12}", end="")
        if index % 10 == 0:
            print()
    print()

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Nhập số nguyên n (2 <= n <= 10): "))
            if 2 <= n <= 10:
                break
            print("Vui lòng nhập đúng trong khoảng [2, 10]!")
        except ValueError:
            print("Dữ liệu nhập vào phải là số nguyên!")

    cau_a = generate_strobogrammatic(n, is_extended=False)
    output_format(cau_a, f"a.- Tất cả các số strobogrammatic gồm {n} chữ số")

    cau_b = generate_strobogrammatic(n, is_extended=True)
    output_format(cau_b, f"b.- Tất cả các số strobogrammatic mở rộng gồm {n} chữ số")