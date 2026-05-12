def giai_quyet_doi_tien(so_tien_thoi):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tong_so_to = 0
    so_loai_tien = 0
    
    print(f"\nSo tien {so_tien_thoi} duoc doi thanh:")
    for m in menh_gia:
        so_to = so_tien_thoi // m
        so_tien_thoi %= m
        
        if so_to > 0:
            print(f"Loai {m} gom {so_to} to")
            tong_so_to += so_to
            so_loai_tien += 1
            
    print(f"TONG CONG CO {tong_so_to} TO")
    print(f"Tong so loai = {so_loai_tien}")

def main():
    try:
        a = int(input("Nhap so tien hang (a): "))
        b = int(input("Nhap so tien khach tra (b): "))
    except ValueError:
        print("Vui long nhap so nguyen hop le!")
        return

    if a > b:
        print(f"Khach hang con thieu: {a - b}")
    elif a == b:
        print("Cam on khach hang. Hen gap lai")
    else:
        so_tien_thoi = b - a
        print(f"So tien can thoi lai cho khach: {so_tien_thoi}")
        
        giai_quyet_doi_tien(so_tien_thoi)
        
        input("\nNhan Enter de ket thuc...")
        print("Cam on khach hang. Hen gap lai")

if __name__ == "__main__":
    main()