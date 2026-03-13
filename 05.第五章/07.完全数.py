# 当整数n的正因数的总和等于n时，n就是完全数。例如，28是一个完全数，因为其正因数是1、2、4、7和14，1+2+4+7+14 =28。编写一个函数，来确定某正整数是否为完全数。
# 函数接收一个参数。如果参数是完全数，函数将返回True，否则返回 False。
# 编写一个main程序，使用函数来识别和显示1到10000之间的所有完全数。
def is_perfect(n):
    result = []

    for i in range(1, n):
        if n % i == 0:
            result.append(i)

    if sum(result) == n:
        return True
    else:
        return False

def main():
    for i in range(1, 10001):
        if is_perfect(i):
            print(i)

main()
