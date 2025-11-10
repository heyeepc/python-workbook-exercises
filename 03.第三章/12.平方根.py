# 编写一个实现牛顿方法的程序，来计算和显示用户输入的数字x的平方根。
# 读取用户输入的x,初始化 guess为x/2,若 guess还不够好,将 guess更新为,guess 和x/guess的平均值
# 计算平方根（牛顿法）

x = float(input("请输入一个数字: "))

# 初始猜测
guess = x / 2

# 迭代直到足够接近
while abs(guess * guess - x) > 1e-6:  # 精度要求可调整
    guess = (guess + x / guess) / 2

print("平方根的近似值为:", guess)
