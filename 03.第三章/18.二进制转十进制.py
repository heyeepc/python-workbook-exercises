# 编写一个程序，将二进制数（以2为基数）转换为十进制数（以10为基数）。程序应该先以字符串形式读取用户输入的二进制数。
# 然后通过处理二进制数中的每个数字，来计算等效的十进制数。最后，程序应该使用适当消息来显示等效的十进制数。
a = list(input("输入一串二进制"))
b = -1
c = 0
print(a)
for z in a[::-1]:
    b = b + 1
    if z == "1":
        c = c + 2**b
print(c)

binary = input("输入一串二进制: ")
decimal = 0

for i, bit in enumerate(binary[::-1]):
    if bit == "1":
        decimal += 2 ** i

print(decimal)
