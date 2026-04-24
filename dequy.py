def tinh_tong_chu_so(n):
    if n<10:
        return n
    return(n%10) + tinh_tong_chu_so(n//10)
print(tinh_tong_chu_so(345))