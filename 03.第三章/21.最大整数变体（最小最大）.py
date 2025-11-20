import random

# 随机生成第一个整数作为初始值
first = random.randint(1, 100)
current_max = first
current_min = first

print(f"初始值: {first}  ← 初始值")

update_count_1 = 0  # 最小值更新次数
update_count_2 = 0  # 最大值更新次数

# 再生成 99 个整数
for i in range(99):
    num = random.randint(1, 100)

    if num < current_min:                 # 新最小值
        current_min = num
        update_count_1 += 1
        print(f"{num}  ← 新最小值")
    elif num > current_max:               # 新最大值
        current_max = num
        update_count_2 += 1
        print(f"{num}  ← 新最大值")
    else:
        print(num)

# 显示最终结果
print("\n最终最大值:", current_max)
print("最终最小值:", current_min)
print("最大值更新次数:", update_count_2)
print("最小值更新次数:", update_count_1)
