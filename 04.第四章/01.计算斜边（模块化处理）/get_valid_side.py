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
