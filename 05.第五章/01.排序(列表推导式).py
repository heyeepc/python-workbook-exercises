numbers = []
print("输入0结束")

while (user_input := input("输入数字: ")) != '0':
    if user_input.isdigit():
        numbers.append(int(user_input))
    else:
        print("请输入有效数字")

print(sorted(numbers))
