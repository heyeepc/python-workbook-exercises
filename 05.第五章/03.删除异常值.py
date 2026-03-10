# 在分析作为科学实验的一部分收集的数据时，在进行其他计算之前，最好先去掉最极端的值。编写一个函数，该函数接收一个值列表和一个非负整数n作为参数。
# 该函数应该创建一个新的列表副本，删除其中的n个最大元素和n个最小元素。然后它应该返回列表的新副本作为函数的唯一结果。返回列表中元素的顺序不必与原始列表中元素的顺序匹配。
# 编写一个main程序来演示函数。它应该从用户那里读取一个数字列表，并通过调用前面描述的函数，从该列表中删除两个最大和两个最小的值。
# 显示删除了异常值的列表，然后显示原始列表。如果用户输入的值小于4，则程序应该生成适当的错误消息。
def remove_extreme_values(data, n):
    # 创建列表副本
    new_list = data.copy()

    # 排序方便删除极值
    new_list.sort()

    # 删除 n 个最小值
    for i in range(n):
        new_list.pop(0)

    # 删除 n 个最大值
    for i in range(n):
        new_list.pop()

    return new_list
    
#切片
#def remove_extreme_values(data, n):
    #return sorted(data)[n:-n]
def main():
    # 读取用户输入
    user_input = input("请输入一组数字（用空格分隔）：")
    numbers = [float(x) for x in user_input.split()]

    # 检查数据量
    if len(numbers) < 4:
        print("错误：至少需要输入4个数字。")
        return

    # 调用函数
    trimmed_list = remove_extreme_values(numbers, 2)

    # 输出结果
    print("删除异常值后的列表：", trimmed_list)
    print("原始列表：", numbers)


if __name__ == "__main__":
    main()
