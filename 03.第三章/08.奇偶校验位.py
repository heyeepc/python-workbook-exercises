# 编写一个程序，使用偶数奇偶校验为用户输入的一组8位计算奇偶校验位。程序应该读取包含8位的字符串，直到用户输入空行为止。
# 在用户输入每个字符串之后，程序应该显示一条明确的消息，指示奇偶校验位应该是0还是1。如果用户输入的不是8位，则显示适当的错误消息。

while True:
    a = input("输入8位二进制")

    if a == "":
        print("程序结束。")
        break

    if len(a) != 8:
        print(" 错误：输入长度不是8位。请重新输入。")
        continue  # 跳过当前循环，进入下一次输入

    ones_count = a.count("1")
    zeros_count = a.count("0")

    if ones_count + zeros_count != 8:
        print("错误：请输入只包含 '0' 或 '1' 的8位数字。")
        continue  # 跳过当前循环，进入下一次输

    if ones_count % 2 == 0:
        parity_bit = 0
        print(f" 计算结果：'1' 的数量 ({ones_count}) 是偶数。")
        print(f" 奇偶校验位应该是 {parity_bit}")
        print(f"带校验位的数据：{a}{parity_bit}")

    else:
        # 当前 '1' 的数量是奇数，所以校验位是 1
        parity_bit = 1
        print(f"计算结果：'1' 的数量 ({ones_count}) 是奇数。")
        print(f"奇偶校验位应该是 {parity_bit}")
        print(f"带校验位的数据：{a}{parity_bit}")
