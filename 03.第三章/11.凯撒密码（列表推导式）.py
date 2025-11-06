# 编写一个实现凯撒密码的程序。允许用户提供消息和移位量，然后显示移位后的消息。确保程序同时编码大写和小写字母。程序还应该支持负移位值，以便它既可以用于编码消息，也可以用于解码消息。
message = input("输入要被加密的字符：")
shift = int(input("输入偏移量："))

result = ""

for ch in message:
    if 'a' <= ch <= 'z':  # 小写字母
        result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':  # 大写字母
        result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    else:  # 非字母字符保持不变
        result += ch

print("加密后的结果：", result)
