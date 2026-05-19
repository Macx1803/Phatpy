import math
def helper  (n,max_len):
    if n==0:
        return [""]
    if n==1:
        return["0","1","8"]
    
    sub_list = helper(n-2,max_len)
    result =[]
    
    for s in sub_list:
        if n != max_len:
            result.append("0"+s+"0")
            
        result.append("1"+s+"1")
        result.append("8"+s+"8")
        result.append("6"+s+"9")
        result.append("9"+s+"6")
    return result

def tim_strobogrammatic(max_digits):
    all_number = ["0"]
    
    for i in range(1, max_digits+1):
        current_len_list = helper(i, i)
        for s in current_len_list:
            if len(s)>1 and s[0] == '0':
                continue
            if s != "0":
                all_number.append(s)
    return all_number

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Kiểm tra các ước số dạng 6k +/- 1
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

if __name__ == "__main__":
    max_digits = 6
    # 1. Sinh danh sách số strobogrammatic dưới dạng chuỗi
    all_strobo_strings = tim_strobogrammatic(max_digits)
    
    # 2. Chuyển thành số nguyên, loại bỏ trùng lặp nếu có và lọc số nguyên tố
    strobo_primes = []
    for s in all_strobo_strings:
        num = int(s)
        if is_prime(num):
            strobo_primes.append(num)
            
    strobo_primes.sort()

    # 4. In kết quả đầu ra
    print("Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu là:")
    print(", ".join(map(str, strobo_primes)))
    print(f"\nTổng cộng có: {len(strobo_primes)} số.")     