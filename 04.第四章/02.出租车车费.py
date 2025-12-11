# 在一个特定的司法管辖区，出租车费包括基本车费$4.00，每行驶140米另加$0.25。编写一个函数，该函数将旅行距离（以公里为单位）作为唯一参数，并返回总车费作为唯一结果。编写一个main程序来演示这个函数。

def Fare(km):
    base = 4.00
    extra_unit_km = 0.14  # 每 0.14 公里加一次钱
    extra_per_unit = 0.25

    extra_units = km / extra_unit_km
    total = base + extra_units * extra_per_unit
    return total

if __name__ == '__main__':
    km = 1.0  # 举例: 1公里
    print(f"行驶 {km} 公里，车费是 ${Fare(km):.2f}")
