# 为赢得某项彩票的头奖，必须将彩票上的所有6个数字与彩票组织者抽到的1~49之间的6个数字匹配。编写一个程序，生成随机选择6个数字的彩票。确保所选的6个数字不包含任何重复。按升序显示数字。

import random

numbers = random.sample(range(1, 50), 6)

print(sorted(numbers))
