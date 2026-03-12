# 创建一个程序，从用户处读取整数，直到输入空行。一旦所有整数都被读取，程序应该显示所有负数，然后是所有的零，最后是所有正数。在每个组中，数字应该按照用户输入的顺序显示。
# 例如，如果用户输入值3、-4、1、0、-1、0和-2，则程序应该输出值-4、-1、-2、0、0、3和1。程序应该将每个值显示在单独一行上。
numbers = []

while True:
    s = input("输入整数，直接回车结束：")

    if s == "":
        break

    try:
        num = int(s)
        numbers.append(num)
    except ValueError:
        print("请输入有效整数！")

negatives = []
zeros = []
positives = []

for n in numbers:
    if n < 0:
        negatives.append(n)
    elif n == 0:
        zeros.append(n)
    else:
        positives.append(n)

for n in negatives + zeros + positives:
    print(n)
