# 计算斜边的函数
def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def main():
    while True:

        print("\n1 - 单次计算")
        print("2 - 循环模式")
        print("q - 退出程序")
        choice = input("请选择模式：").strip().lower()

        if choice == 'q':
            print("程序已退出")
            break

        elif choice == '1':
            a_input = input("请输入第一个直角边的长度 (或输入 'q' 退出): ").strip()

            if a_input.lower() == 'q':
                break

            b_input = input("请输入第二个直角边的长度 (或输入 'q' 退出): ").strip()

            if b_input.lower() == "q":
                break

            try:

                a = float(a_input)
                b = float(b_input)

                if a < 0 or b < 0:
                    print("不能小于0")
                    continue

                if a == 0 or b == 0:
                    print("边不能为 0")
                    continue

                c = hypotenuse(a, b)
                print(f"a = {a:.2f}")
                print(f"b = {b:.2f}")
                print(f"c² = a² + b² = {a**2:.2f} + {b**2:.2f} = {c**2:.2f}")
                print(f"c ={c:.2f}")
                print(f"斜边的长度是：{c:.2f}\n")

            except ValueError:
                print("输入正确的数字")


if __name__ == "__main__":
    main()
