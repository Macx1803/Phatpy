def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Bước 1: Nhập dữ liệu
numbers = []
while True:
    try:
        num = int(input("Nhập một số nguyên: "))
        numbers.append(num)
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")
        continue
    
    choice = input("Bạn có muốn tiếp tục nhập không? (Y/N): ").strip().upper()
    if choice == 'N':
        break

print("\n--- KẾT QUẢ ---")

# a) In ra các số nguyên tố có trong list
primes = [x for x in numbers if is_prime(x)]
print(f"a) Các số nguyên tố trong list: {primes}")

# b) Tính trung bình cộng các số âm, trung bình cộng các số dương
negatives = [x for x in numbers if x < 0]
positives = [x for x in numbers if x > 0]

avg_neg = sum(negatives) / len(negatives) if negatives else 0
avg_pos = sum(positives) / len(positives) if positives else 0

print(f"b) Trung bình cộng số âm: {avg_neg}")
print(f"   Trung bình cộng số dương: {avg_pos}")

# c) Số lớn nhất, số nhỏ nhất
if numbers:
    print(f"c) Số lớn nhất: {max(numbers)}")
    print(f"   Số nhỏ nhất: {min(numbers)}")

# d) Kiểm tra list đã được sắp xếp tăng dần hay chưa
is_sorted = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
if is_sorted:
    print("d) List đã được sắp xếp tăng dần.")
else:
    print("d) List chưa được sắp xếp tăng dần.")