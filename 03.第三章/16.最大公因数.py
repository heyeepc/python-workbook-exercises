a = int(input("输入一个数: "))
b = int(input("输入第二个数: "))

while b != 0:
    r = a % b
    a = b
    b = r
print(f"最大公约数是 {a}")
