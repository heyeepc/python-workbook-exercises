# 编写一个函数，以直角三角形的两个直角边的长度为参数。返回使用勾股定理计算的三角形的斜边作为函数的结果。包含一个main程序，它从用户那里读取直角三角形中直角边的长度，使用函数计算斜边的长度，并显示结果。
import math

# 计算斜边的函数
def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def main():
    a = float(input("请输入第一个直角边的长度："))
    b = float(input("请输入第二个直角边的长度："))
    
    c = hypotenuse(a, b)
    print(f"斜边的长度是：{c}")

if __name__ == "__main__":
    main()
