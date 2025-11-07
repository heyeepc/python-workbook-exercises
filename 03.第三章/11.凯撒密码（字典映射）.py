shift = int(input("输入偏移量："))
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 构造映射表
table = str.maketrans(
    alphabet_lower + alphabet_upper,
    alphabet_lower[shift % 26:] + alphabet_lower[:shift % 26] +
    alphabet_upper[shift % 26:] + alphabet_upper[:shift % 26]
)

message = input("输入要被加密的字符：")
print(message.translate(table))
