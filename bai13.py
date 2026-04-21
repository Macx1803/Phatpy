import re

def chuan_hoa_chuoi(s):

    lines = s.splitlines()
    ket_qua_dong = []

    for line in lines:
        line = line.strip()
        line = re.sub(r'\s+', ' ', line)
        line = re.sub(r'\s+([.,])', r'\1', line)
        if line: 
            ket_qua_dong.append(line)
    return "\n".join(ket_qua_dong)
du_lieu_vao = """
    Quê hương
Quê  hương  là   chùm  khế   ngọt.
   Cho  con  trèo  hái   mỗi   ngày   .
Quê   hương  là   đường  đi   học  .
  Con  về  rợp  bướm   vàng  bay  .
 Đỗ     Trung  Quân   
"""

print("chuoi sau khi chuan hoa")
print(chuan_hoa_chuoi(du_lieu_vao))