
# 本练习将创建一个程序，从用户处读取单词，直到用户输入空行。在用户输入空白行之后，程序应该显示一次用户输入的每个单词。单词应该按照它们最初输入的顺序显示。

words = []

print("请输入单词（输入空行以结束，重复单词将只保留第一个）：")

while True:
    line = input("> ").strip() # strip() 可以去除首尾空格
    
    if line == "":
        break
    
    # 核心逻辑：只有当单词不在列表中时才添加
    if line not in words:
        words.append(line)

print("\n你输入的唯一单词（按输入顺序）：")
for word in words:
    print(word)
