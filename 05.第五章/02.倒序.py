#编写一个程序，从用户处读取整数，并将它们存储在一个列表中。使用0作为标记值来标记输入的结束。一旦所有值都被读取，程序应该以相反的顺序显示它们（除了0），每行显示一个值。
numbers = []

print("请输入整数（输入 0 结束）：")

while True:
    try:
        # 读取用户输入并转换为整数
        user_input = int(input("> "))

        # 如果输入是 0，则跳出循环
        if user_input == 0:
            break

        # 将输入的数字添加到列表中
        numbers.append(user_input)
    except ValueError:
        print("请输入有效的整数！")


sorted_numbers = sorted(numbers, reverse=True)

for num in sorted_numbers:
    print(num)
