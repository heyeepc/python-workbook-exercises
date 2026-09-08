# 编写一个程序,从用户处读取值,直到输入空行为止。显示用户输入的所有值的总和(如果输入的第一个值是空行,则为0.0)。使用递归完成此任务。程序可能不使用任何循环。
def sum_inputs():
    # 读取用户输入并去除首尾空白字符
    user_input = input("请输入数值（输入空行结束）: ").strip()
    
    # 终止条件：如果是空行，返回 0.0
    if user_input == "":
        return 0.0
    
    # 递归步骤：当前数值 + 剩余输入的累加和
    return float(user_input) + sum_inputs()


if __name__ == "__main__":
    total = sum_inputs()
    print(f"输入所有值的总和为: {total}")
