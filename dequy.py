def tinh_tong_chu_so(n):
    if n<10:
        return n
    return(n%10) + tinh_tong_chu_so(n//10)
print(tinh_tong_chu_so(345))


def giai_thua(n):
    if n== 0 or n==1:
        return n
    return n * giai_thua(n -1)
print(giai_thua(5))


def tinh_luy_thua(a,b):
    if b == 0:
        return 1
    return a * tinh_luy_thua(a, b - 1)

print(tinh_luy_thua(2, 3))

def tim_gcd(a, b):
    if b == 0:
        return a
    return tim_gcd(b, a % b)

print(tim_gcd(48, 18))
