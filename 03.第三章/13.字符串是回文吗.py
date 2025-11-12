# 如果一个字符串向前读取和向后读取的内容是相同的，那么它就是回文（palindrome）。
# 例如anna、civic、level 和 hannah都是回文词。编写一个程序，从用户那里读取一个字符串，并使用循环来确定它是否是一个回文。显示结果，包括有意义的输出消息。
# 判断字符串是否是回文

s = input("请输入一个字符串：")

# 预处理（可选）：去除空格并统一大小写
s = s.replace(" ", "").lower()

is_palindrome = True  # 假设是回文

# 从两头向中间比较
for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"'{s}' 是回文字符串。")
else:
    print(f"'{s}' 不是回文字符串。")
