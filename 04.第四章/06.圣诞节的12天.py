# 编写一个程序，显示《圣诞节的12天》的完整歌词。程序应该包含一个函数来显示歌词。它将把段号作为唯一的参数。然后程序应该用从1到12的整数调用这个函数12次。 
# 歌曲中发送给收件人的每个条目应该只在程序中出现一次，鹧鸪可能除外。
# 如果这能帮助处理第一段“A partridge in a pear tree”和第二段“And a partridge in a pear tree”之间的区别，它可能会出现两次。

def sing_verse(day):
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    gifts = [
        "a partridge in a pear tree",
        "two turtle doves",
        "three French hens",
        "four calling birds",
        "five gold rings",
        "six geese a-laying",
        "seven swans a-swimming",
        "eight maids a-milking",
        "nine ladies dancing",
        "ten lords a-leaping",
        "eleven pipers piping",
        "twelve drummers drumming"
    ]

    print(f"On the {days[day - 1]} day of Christmas my true love sent to me:")

    for i in range(day - 1, -1, -1):
        if i == 0 and day != 1:
            print(f"And {gifts[i]}.")
        else:
            print(f"{gifts[i].capitalize()}.")


# 主程序：调用 12 次
for day in range(1, 13):
    sing_verse(day)
    print()
