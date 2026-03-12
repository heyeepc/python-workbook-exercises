numbers = []

while True:
    s = input("输入整数，直接回车结束：")
    if s == "":
        break
    numbers.append(int(s))

negatives = [n for n in numbers if n < 0]
zeros = [n for n in numbers if n == 0]
positives = [n for n in numbers if n > 0]

for n in negatives + zeros + positives:
    print(n)
