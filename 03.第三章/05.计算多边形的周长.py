# 编写一个计算多边形周长的程序。首先从用户处读取多边形周长上的第一个点的x和y坐标。然后继续读取值对，直到用户为x坐标输入空行为止。
# 每次读取一个额外坐标，都应该计算到前一个点的距离，并把它加到周长上。为x坐标输入空行时，程序应该将最后一点到第一点的距离加到周长上。
# 然后显示周长。用户输入的值以粗体显示。

import math

print("请输入多边形各顶点坐标（按顺序），输入空行结束。")

# 读取第一个点
x1 = input("x1: ")
if x1 == "":
    print("未输入任何点。")
    exit()

y1 = input("y1: ")
if y1 == "":
    print("未输入任何点。")
    exit()

first_x, first_y = float(x1), float(y1)
prev_x, prev_y = first_x, first_y
perimeter = 0.0

# 读取后续点
while True:
    x = input("x: ")
    if x == "":  # 空行结束
        break
    y = input("y: ")
    if y == "":
        break

    x, y = float(x), float(y)
    # 计算当前点与前一个点的距离
    distance = math.hypot(x - prev_x, y - prev_y)
    perimeter += distance

    prev_x, prev_y = x, y

# 最后加上最后一点到第一点的距离
perimeter += math.hypot(first_x - prev_x, first_y - prev_y)

print(f"多边形的周长为：{perimeter:.2f}")
