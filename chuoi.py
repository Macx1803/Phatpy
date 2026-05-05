from collections import Counter

s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")

counter1 = Counter(s1)
counter2 = Counter(s2)
common_chars = counter1 & counter2

print("\na) Những ký tự xuất hiện trong cả 2 chuỗi:")
print(list(common_chars.keys()))


dict1 = {char: s1.count(char) for char in set(s1)}
dict2 = {char: s2.count(char) for char in set(s2)}

only_in_s1 = [char for char in dict1 if char not in dict2]

only_in_s2 = [char for char in dict2 if char not in dict1]

print(f"\nb) Số ký tự có trong S1 nhưng không có trong S2: {len(only_in_s1)}")
print(f"   Số ký tự có trong S2 nhưng không có trong S1: {len(only_in_s2)}")

print("\nc) Những ký tự chỉ có trong S1 (không có trong S2):")
print(only_in_s1)
print("   Những ký tự chỉ có trong S2 (không có trong S1):")
print(only_in_s2)