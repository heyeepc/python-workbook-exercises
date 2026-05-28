# 用英语编写一个项列表时，通常用逗号分隔各个项。此外，and一词通常包括在最后一项之前，除非列表只包含一项。
# 编写一个函数，将字符串列表作为它的唯一参数。函数应该返回一个字符串，该字符串包含列表中的所有项，按照前面描述的方式进行格式化，作为它的唯一结果。虽然在前面展示的示例中，列表只包含四个或更少的元素，但是对于任何长度的列表，函数的行为都应该是正确的。
# 包含一个main程序，它从用户处读取几个项，通过调用函数对它们进行格式化，然后显示函数返回的结果。
def format_list(items):
    """将列表项格式化为带 'and' 的英文叙述字符串。"""
    n = len(items)
    
    if n == 0:
        return ""
    if n == 1:
        return items[0]
    if n == 2:
        return f"{items[0]} and {items[1]}"
    
    # 处理 3 个及以上元素的情况
    # 使用逗号连接除最后一个外的所有项，并在最后一项前加 "and"
    prefix = ", ".join(items[:-1])
    return f"{prefix} and {items[-1]}"

def main():
    str_list = []
    print("请输入列表项（直接按回车键结束输入）：")
    
    while True:
        user_input = input("输入项: ").strip()
        
        # 如果输入为空字符串，则停止输入
        if user_input == "":
            break
            
        str_list.append(user_input)

    # 调用函数并打印结果
    result = format_list(str_list)
    if result:
        print("\n格式化后的结果：")
        print(result)
    else:
        print("\n列表为空。")

if __name__ == '__main__':
    main()
