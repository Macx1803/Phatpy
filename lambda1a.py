tri_tuyet_doi = lambda n : n if n>= 0 else -n
print(tri_tuyet_doi(-30))
print(tri_tuyet_doi(10))

cong_15 = lambda n: n + 15
print(cong_15(10))

tinh_tich = lambda x,y : x*y
print(tinh_tich(5,6))

kiem_tra_boi = lambda n : n % 13 ==0 or n % 19 ==0
print(kiem_tra_boi(26))
print(kiem_tra_boi(19))
print(kiem_tra_boi(20))