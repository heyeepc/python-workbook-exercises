def get_valid_side(prompt):
    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == 'q':
            return None

        try:
            value = float(user_input)

            if value <= 0:
                print("边必须大于 0")
                continue

            return value

        except ValueError:
            print("请输入正确数字")
            
def single_mode():
    a = get_valid_side("请输入第一个直角边（q退出）：")
    if a is None:
        return

    b = get_valid_side("请输入第二个直角边（q退出）：")
    if b is None:
        return

    c = hypotenuse(a, b)
    print(f"斜边的长度是：{c:.2f}\n")



def loop_mode():
    while True:
        a = get_valid_side("请输入第一个直角边（q退出）：")
        if a is None:
            break

        b = get_valid_side("请输入第二个直角边（q退出）：")
        if b is None:
            break

        c = hypotenuse(a, b)
        print(f"斜边的长度是：{c:.2f}\n")

def show_menu():
    print("\n====== 菜单 ======")
    print("1 - 单次计算")
    print("2 - 循环模式")
    print("q - 退出程序")
    print("==================")
