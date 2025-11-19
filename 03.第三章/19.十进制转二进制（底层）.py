n = int(input("输入十进制整数: "))
if n == 0:
    print("0")
else:
    bits = []
    while n > 0:
        bits.append(str(n & 1))  # 取最低位
        n >>= 1                  # 右移一位
    print("".join(bits[::-1]))
