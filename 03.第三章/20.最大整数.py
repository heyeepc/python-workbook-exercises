# 本练习检查确定整数集合中最大值的过程。每个整数都从1到100之间的数字中随机选择。整数集合可能包含重复的值，也可能不包括一些介于1和100之间的整数。
# 创建一个程序，先选择1到100之间的随机整数，将该整数保存为到目前为止遇到的最大数字。选择初始整数后，生成1到100之间的另外99个随机整数。在生成每个整数时检查它，看看它是否大于目前遇到的最大数字。\
# 如果是，那么程序应该更新遇到的最大数字，并计算执行更新的次数。生成后显示每个整数。包含一个表示新的最大值的整数符号。
import random

# 随机生成第一个整数作为初始最大值
current_max = random.randint(1, 100)
print(f"初始值: {current_max}  ← 初始最大值")
update_count = 0

# 再生成 99 个整数
for i in range(99):
    num = random.randint(1, 100)

    # 检查是否为新的最大值
    if num > current_max:
        current_max = num
        update_count += 1
        print(f"{num}  ← 新最大值")
    else:
        print(num)

# 显示最终结果
print("\n最终最大值:", current_max)
print("最大值更新次数:", update_count)
