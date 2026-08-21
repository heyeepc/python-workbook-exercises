keypad = {
    '1': ".,?!:",
    '2': "ABC",
    '3': "DEF",
    '4': "GHI",
    '5': "JKL",
    '6': "MNO",
    '7': "PQRS",
    '8': "TUV",
    '9': "WXYZ",
    '0': " "
}

user_input = input("请输入消息: ").upper()
result = ""

for char in user_input:
    # 挨个遍历 keypad 的每个按键
    for digit, symbols in keypad.items():
        if char in symbols:
            # .find(char) 能直接拿到字符在字符串里的索引位置（从0开始）
            # 索引 + 1 就是需要按键的次数
            count = symbols.find(char) + 1
            result += digit * count
            break  # 找到了就跳出当前 key 的查找

print("按键序列:", result)
