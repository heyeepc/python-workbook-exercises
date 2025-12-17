import statistics

def get_median_builtin(a, b, c):
    return statistics.median([a, b, c])

if __name__ == '__main__':
    a = float(input("输入数字a: "))
    b = float(input("输入数字b: "))
    c = float(input("输入数字c: "))

    A = Median(a, b, c)
    print(f"中位数是 {A}")
