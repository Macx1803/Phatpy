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