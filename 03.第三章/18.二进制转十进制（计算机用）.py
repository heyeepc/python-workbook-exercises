binary = input("输入一串二进制: ")
decimal = 0

for bit in binary:
    decimal = decimal * 2 + int(bit)

print(decimal)
