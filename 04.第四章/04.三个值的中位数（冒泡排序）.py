# 编写一个函数，以三个数字为参数，并返回这些参数的中值作为其结果。包含一个main程序，从用户读取三个值，并显示它们的中位数。
def Median(a, b, c):
    nums = [a, b, c]

    # 简单冒泡排序（两轮就够）
    for _ in range(2):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums[1]   # 中位数


if __name__ == '__main__':
    a = float(input("输入数字a: "))
    b = float(input("输入数字b: "))
    c = float(input("输入数字c: "))

    A = Median(a, b, c)
    print(f"中位数是 {A}")
