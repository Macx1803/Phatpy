def decompressText(cipher_text):
    plain_text = ""
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            count = int(cipher_text[i+1])
            char = cipher_text[i+2]
            plain_text += char * count  
            i += 3
        else:
            plain_text += cipher_text[i]
            i += 1
    return plain_text

test_cases= [
    "XY#6Z1#4023",
    "#39+1=1#30"
]
for text in test_cases:
    print(f"Cipher: {text} -> Plain: {decompressText(text)}")