# 创建一个程序，使用 Python的随机数生成器模拟抛硬币几次。模拟的硬币应该是公平的，这意味着正面的概率等于反面的概率。程序应该投掷模拟的硬币，直到出现3个连续的正面和3个连续的反面。
# 每次结果为正面时显示一个H，每次结果为反面时显示一个T，模拟的所有结果都在同一行上。然后显示连续出现3次相同结果所需的投掷次数。
# 当程序运行时，它应该执行模拟10次，并报告所需的平均投掷次数。
import random

def simulate_once():
    count = 0          # 总投掷次数
    heads = 0          # 当前连续正面数
    tails = 0          # 当前连续反面数
    results = []        # 存放 H/T

    while True:
        flip = random.randint(0, 1)
        count += 1

        if flip == 0:
            results.append("H")
            heads += 1
            tails = 0
        else:
            results.append("T")
            tails += 1
            heads = 0

        # 同时满足：必须出现过3个H 和 3个T
        if heads == 3 and "TTT" in "".join(results):
            break
        if tails == 3 and "HHH" in "".join(results):
            break

    print("".join(results))
    return count


total = 0

for i in range(10):
    total += simulate_once()

print(f"平均投掷次数: {total/10:.2f}")
