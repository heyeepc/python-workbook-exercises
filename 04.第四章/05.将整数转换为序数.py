# 像第一、第二和第三这样的词被称为序数。本练习将编写一个函数，该函数的唯一参数为整数，并返回一个包含对应英文序号的字符串作为唯一结果。函数必须处理1到12（含）之间的整数。
# 如果函数调用的参数不在这个范围内，那么它应该返回一个空字符串。包含一个main程序，显示从1到12的每个整数及其序号来演示函数。
# main程序应该只在文件没有被导入其他程序时运行。
def ordinal_english(n: int) -> str:
    """
    接收一个整数 n
    如果 n 在 1 到 12 之间，返回对应的英文序数词
    否则返回空字符串
    """
    ordinals = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }

    return ordinals.get(n, "")


def main():
    # 显示 1 到 12 的整数及其英文序数
    for i in range(1, 13):
        print(i, ordinal_english(i))


# 只有在该文件被直接运行时才执行 main
if __name__ == "__main__":
    main()
