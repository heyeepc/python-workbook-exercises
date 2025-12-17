def get_median_sort(a, b, c):
    lst = [a, b, c]
    lst.sort()
    return lst[1]

if __name__ == '__main__':
    a = float(input("输入数字a: "))
    b = float(input("输入数字b: "))
    c = float(input("输入数字c: "))

    A = Median(a, b, c)
    print(f"中位数是 {A}")
