# 编写一个程序，从用户那里读取价格，直到输入空行为止。在一行显示所有输入项的总成本，在第二行显示客户用现金支付的应付金额。现金付款的金额应四舍五入到最接近的5美分。
# 计算现金支付金额的一种方法是首先确定总共需要支付多少便士。
# 然后计算总便士数除以5的余数。最后，如果余数小于2.5，则向下调整总数。否则向上调整总数。

total_cost = 0.0

while True:
    try:
        price_input = input("价格 ($): )")
        if price_input == "":
            break

        price = float(price_input)
        total_cost += price


    except ValueError:
        print("输入无效。请输入数字价格或空行结束。")
        continue


total_cents = round(total_cost * 100)

remainder = total_cents % 5

if remainder < 2.5:
    cash_cents = total_cents - remainder
else:
    cash_cents = total_cents + (5 - remainder)

cash_payment = cash_cents / 100.0

print(f"所有输入项的总成本是: ${total_cost:.2f}")
print(f"客户用现金支付的应付金额**（四舍五入到最近的 5¢）是: ${cash_payment:.2f}")
