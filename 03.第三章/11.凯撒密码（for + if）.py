message = input("输入要被加密的字符：")
shift = int(input("输入偏移量："))

result = ""  # 用来保存最终的字符串

for ch in message:
    if ch >= 'a' and ch <= 'z':   # 小写字母
        # ord(ch) - ord('a') 得到字母在字母表的位置(0-25)
        # 加上偏移后取模，再转回字母
        new_code = (ord(ch) - ord('a') + shift) % 26 + ord('a')
        result = result + chr(new_code)
    elif ch >= 'A' and ch <= 'Z':  # 大写字母
        new_code = (ord(ch) - ord('A') + shift) % 26 + ord('A')
        result = result + chr(new_code)
    else:
        # 非字母，不加密，直接保留
        result = result + ch

print("加密后的结果：", result)
