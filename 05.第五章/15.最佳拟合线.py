# 最佳拟合线是最接近n个数据点集合的直线。在这个练习中，假设集合中的每个点都有一个x坐标和一个y坐标。符号x和y分别表示集合中的x平均值和y平均值。
# 编写一个程序，从用户处读取点的集合。用户在单独一行上输入第一个x坐标，然后在另一行上输入第一个y坐标。
# 允许用户继续输入坐标，在单独的行上输入x和y值，直到程序为x坐标读取空行为止。以y=mx+b的形式显示最佳拟合线的公式，用前面公式计算的值替换m和b。
# 例如，如果用户输入坐标（1，1）、（2，2.1）和（3，2.9），则程序应该显示y=0.95x+0.1。

def main():
    x_values = []
    y_values = []
    
    print("请输入数据点（直接在x坐标处按回车结束输入）：")
    
    while True:
        # 读取 x 坐标
        x_input = input("请输入 x 坐标: ").strip()
        
        # 如果用户在 x 坐标输入空行，则停止输入
        if x_input == "":
            break
            
        # 读取 y 坐标
        y_input = input("请输入 y 坐标: ").strip()
        
        try:
            x = float(x_input)
            y = float(y_input)
            x_values.append(x)
            y_values.append(y)
        except ValueError:
            print("输入无效，请输入数字。")
            continue

    n = len(x_values)
    
    # 至少需要两个点才能确定一条直线
    if n < 2:
        print("错误：计算最佳拟合线至少需要2个点。")
        return

    # 计算公式所需的各种和
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x_squared = sum(x ** 2 for x in x_values)
    
    # 计算平均值
    avg_x = sum_x / n
    avg_y = sum_y / n
    
    # 分母检查，防止所有 x 坐标都相同导致除以 0
    denominator = sum_x_squared - (sum_x ** 2) / n
    if denominator == 0:
        print("错误：所有 x 坐标都相同，无法计算垂直线的斜率。")
        return

    # 计算斜率 m 和截距 b
    m = (sum_xy - (sum_x * sum_y) / n) / denominator
    b = avg_y - m * avg_x

    # 格式化输出公式
    # 如果 b 是负数，直接显示 - 符号会更美观，这里用 + 号连接，Python 的格式化会自动处理负号
    if b >= 0:
        print(f"最佳拟合线公式为：y = {m:.2f}x + {b:.2f}")
    else:
        print(f"最佳拟合线公式为：y = {m:.2f}x - {abs(b):.2f}")

if __name__ == "__main__":
    main()
