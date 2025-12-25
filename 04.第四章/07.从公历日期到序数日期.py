# 编写一个名为ordinalDate（）的函数，该函数接收三个整数作为参数。这些参数分别为日、月和年。函数应该返回该日期在一年中的序数日期作为唯一结果。
# 创建一个main程序，它读取用户的日期、月份和年份，并显示该日期在一年中的序数日期。main程序应该只在文件没有被导入其他程序时运行。

def is_leap_year(year: int) -> bool:
    """判断是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def ordinalDate(day: int, month: int, year: int) -> int:
    """
    接收 日、月、年
    返回该日期在一年中的序数日期
    """
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[1] = 29

    # 累加之前月份的天数
    ordinal = sum(days_in_month[:month - 1]) + day
    return ordinal


def main():
    day = int(input("请输入日："))
    month = int(input("请输入月："))
    year = int(input("请输入年："))

    result = ordinalDate(day, month, year)
    print(f"{year}-{month}-{day} 是该年的第 {result} 天")


if __name__ == "__main__":
    main()
