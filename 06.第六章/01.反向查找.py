# 编写一个名为reverseLookup（）的函数，查找字典中映射到特定值的所有键。该函数将字典和要搜索的值作为其唯一的参数，从字典中返回一个（可能是空的）键列表，这些键映射到提供的值。
# 包含演示reverseLookup（）函数的main程序，作为本练习的解答的一部分。程序应该创建一个字典，然后在返回多个键、单个键和无键时显示reverseLookup（）函数工作正常。
# 确保main程序只在包含此练习解答的文件未导入其他程序时运行。
def reverseLookup(d, value):
    result = []

    for key in d:
        if d[key] == value:
            result.append(key)

    return result


def main():
    data = {
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 3
    }

    print("查找 value=1（多个key）:")
    print(reverseLookup(data, 1))

    print("查找 value=2（单个key）:")
    print(reverseLookup(data, 2))

    print("查找 value=5（没有key）:")
    print(reverseLookup(data, 5))


if __name__ == "__main__":
    main()
