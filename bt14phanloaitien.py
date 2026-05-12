def doi_tien(x):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tong_so_to = 0
    
    print(f"So tien {x} duoc doi thanh:")
    for m in menh_gia:
        so_to = x // m
        x = x % m
        tong_so_to += so_to
        print(f"Loai {m} gom {so_to} to")
        
    print("-" * 20)
    print(f"TONG CONG CO {tong_so_to} TO")

# Chạy thử
x = int(input("Nhap so tien X: "))
doi_tien(x)