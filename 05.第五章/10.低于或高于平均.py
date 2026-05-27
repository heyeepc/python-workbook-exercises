# 编写一个程序，从用户处读取数字，直到用户输入空行。程序应该显示用户输入的所有值的平均值。
# 然后程序应该显示所有低于平均值的值，然后显示所有平均值（如果有），最后显示所有高于平均值的值。在每个值列表之前应该显示一个适当标签。
# 初始化四个列表，分别用于存储：所有数据、低于平均值、等于平均值、高于平均值
date = []
date_min = []
date_equal = []
date_max = []

while True:
    date_1 = input("输入一个数字（直接回车结束）：")

    # 1. 正确判断空行（直接回车键入的是空字符串 ""）
    if date_1 == "":
        break

    # 2. 将输入的字符串转换为浮点数，并整体添加到列表中
    try:
        num = float(date_1)
        date.append(num)
    except ValueError:
        print("请输入有效的数字！")
        continue

# 确保用户至少输入了一个数字，避免除以零的错误
if len(date) > 0:
    # 3. 计算平均值
    b = sum(date) / len(date)

    # 4. 遍历列表，将数字分类
    for i in date:
        if i < b:
            date_min.append(i)
        elif i == b:
            date_equal.append(i)
        else:
            date_max.append(i)

    # 5. 打印结果（带上适当的标签说明）
    print("--- 统计结果 ---")
    print(f"所有输入的数字的平均值是: {b:.2f}")
    print(f"低于平均值的值: {date_min}")
    print(f"等于平均值的值: {date_equal}")
    print(f"高于平均值的值: {date_max}")
else:
    print("未输入任何数字。")
