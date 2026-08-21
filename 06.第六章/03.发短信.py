# 在一些较旧的手机上,可以用数字键盘发送短信。因为每个键都有多个相关联的字母,所以大多数字母都需要多次按键。按一次数字将生成该键列出的第一个字符。按数字2、3、4或5次会产生第二个、第三个、第四个或第五个字符。
# 编写一个程序,显示用户输入消息所需的按键。构造一个字典,从每个字母或符号映射到生成它所需的按键。然后使用字典创建和显示用户消息所需的按键。
# 例如,如果用户输入 Hello, World!,程序就应该输出 4433555555666110966677755531111。确保程序同时处理大小写字母。忽略上表中没有列出的字符,如分号和括号。

# 1. 建立九宫格映射字典
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

# 2. 构建“字符 -> 按键序列”的反向字典
char_to_presses = {}
for digit, symbols in keypad.items():
    for index, char in enumerate(symbols):
        # index + 1 代表该字符需要连续按该键的次数
        char_to_presses[char] = digit * (index + 1)

# 3. 接收用户输入并转换
user_input = input("请输入消息: ").upper()
result = ""

for char in user_input:
    if char in char_to_presses:
        result += char_to_presses[char]

print("按键序列:", result)
