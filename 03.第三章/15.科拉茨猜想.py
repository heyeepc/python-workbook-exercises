# 创建一个程序，从用户那里读取整数n，并报告从n开始到1结束的序列中的所有值。程序应该允许用户继续输入新的n值（并且应该继续显示序列），直到用户输入一个小于或等于零的n值。
while True:
    n = int(input("请输入一个正整数（输入<=0结束）："))
    if n <= 0:
        print("程序结束。")
        break

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    print("科拉茨序列:", sequence)
