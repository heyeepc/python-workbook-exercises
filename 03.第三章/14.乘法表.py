# 本练习将创建一个显示乘法表的程序，该乘法表显示从1*1
# 到10*10的所有整数组合的乘积。乘法表应该在表的顶部包括一排包含数字1到10的标签。它还应该在左边包括由数字1到10组成的标签。
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 使用嵌套列表推导式生成乘法表（矩阵）
# 外层循环遍历 a (行)，内层循环遍历 b (列)
multiplication_table = [
    [x * y for y in b]
    for x in a
]

# 打印结果（列表的列表形式）
print(multiplication_table)

# 打印一个格式化的表格示例
print("\n--- 格式化输出 (乘法表) ---")
# 打印 B 列表作为列标题
print("   | " + " ".join([f"{val:3}" for val in b]))
print("---+" + "----" * len(b))
for i, row in enumerate(multiplication_table):
    # 打印 A 列表元素作为行标题
    print(f"{a[i]:2} | " + " ".join([f"{val:3}" for val in row]))
