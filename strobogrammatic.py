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

if __name__ == "__main__":
    max_digits = 6
    strobogrammatic_numbers = tim_strobogrammatic(max_digits)

    strobogrammatic_numbers.sort(key=lambda x: (len(x), x))

    print("Các số strobogrammatic nhỏ hơn 1 triệu là:")
    
    for index, num in enumerate(strobogrammatic_numbers, 1):
        print(f"{num:<8}", end="")
        if index % 10 == 0:
            print()           