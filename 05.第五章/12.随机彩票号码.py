# 为赢得某项彩票的头奖，必须将彩票上的所有6个数字与彩票组织者抽到的1~49之间的6个数字匹配。编写一个程序，生成随机选择6个数字的彩票。确保所选的6个数字不包含任何重复。升序显示数字。
import random

a = []
b = []

# 生成 1 到 49 的数字列表
for z in range(1, 50):
    a.append(z)

# 当 b 中的数字不足 6 个时，持续抽取
while len(b) < 6:
    b_1 = random.choice(a)
    b.append(b_1)
    a.remove(b_1)

# 升序打印
print(sorted(b))
