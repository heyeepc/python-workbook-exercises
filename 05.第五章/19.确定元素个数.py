# Python的标准库包含一个名为count（）的方法，它可以确定特定值在列表中出现的次数。这个练习创建一个名为countRange（）的新函数。它确定并返回列表中大于或等于某个最小值而小于某个最大值的元素数。
# 函数接收三个参数：列表、最小值和最大值。它返回一个大于或等于的整数结果。
# 包括一个main程序，为几个不同的列表，最小值和最大值演示函数。确保程序对整数列表和浮点数列表都能正确工作。
def countRange(data_list, min_val, max_val):
    """
    计算列表中大于或等于 min_val 且小于 max_val 的元素数量
    """
    count = 0
    for item in data_list:
        # 注意：左闭右开区间 [min_val, max_val)
        if min_val <= item < max_val:
            count += 1
    return count


if __name__ == '__main__':
    # 测试用例 1：全整数列表
    list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res1 = countRange(list_int, 3, 8)
    print(f"整数列表测试 [3, 8): 符合条件的个数为 {res1} (期待结果: 5)")

    # 测试用例 2：包含浮点数的列表
    list_float = [1.5, 2.3, 3.0, 4.7, 5.5, 6.2]
    res2 = countRange(list_float, 2.3, 5.5)
    print(f"浮点数列表测试 [2.3, 5.5): 符合条件的个数为 {res2} (期待结果: 3)")

    # 测试用例 3：边界值测试（测试是否真正排除了最大值）
    list_boundary = [10, 20, 30, 40]
    res3 = countRange(list_boundary, 10, 30)
    print(f"边界值测试 [10, 30): 符合条件的个数为 {res3} (期待结果: 2)")
