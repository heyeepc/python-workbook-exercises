# 正整数n的正因数是一个小于n、且能整除n的正整数。编写一个函数来计算正整数的所有正因数。该整数作为函数的唯一参数传递。该函数返回一个包含所有正因数的列表，作为其唯一结果。
# 通过编写main程序来完成这个练习，main程序通过从用户处读取一个值，并显示其正因数列表来演示该函数。确保main程序只在解答没有导入另一个文件时运行。
def factors(n):
    result = []

    for i in range(1, n):
        if n % i == 0:
            result.append(i)

    return result


if __name__ == "__main__":
    n = int(input("输入一个正整数: "))
    print(factors(n))
