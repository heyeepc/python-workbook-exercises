n = int(input("请输入一个整数： "))

if n < 2:
    print("错误：请输入一个不小于 2 的整数。")
else:
    factor = 2
    print(f"{n} 的素因子为：")
    while factor * factor <= n:   # 只需试到 sqrt(n)
        if n % factor == 0:
            print(factor)         # 输出一个因子
            n //= factor          # 把因子从 n 中除掉，继续分解
        else:
            factor += 1
    # 如果最后 n > 1，说明剩下的 n 本身是素数
    if n > 1:
        print(n)

