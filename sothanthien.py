import math

def dao_nguoc(n):
    return int(str(n)[::-1])

def la_so_than_thien(n):
    n_dao = dao_nguoc(n)
    return math.gcd(n, n_dao) == 1

def giai_bai_toan():
    try:
        a = int(input("nhap a: "))
        b = int(input("nhap b: "))
        
        if not (10 <= a <= b <= 30000):
            print("vui long nhap dung dieu kien 10 <= a <= b <= 30000")
            return
            
        so_than_thien_list = []
        for i in range(a, b + 1):
            if la_so_than_thien(i):
                so_than_thien_list.append(i)
                
        print("\nCác số thân thiện tìm được:")
        print(*so_than_thien_list)
        print(f"\nSố lượng số thân thiện: {len(so_than_thien_list)}")

    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

giai_bai_toan()