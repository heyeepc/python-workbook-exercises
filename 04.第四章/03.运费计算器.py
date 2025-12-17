# 在线零售商为其许多商品提供快递服务，订单中第一项商品的运费为10.95美元，同一订单中后续每项商品的运费为2.95美元。编写一个函数，以商品的数量作为其唯一的参数。
# 将订单的运费作为函数的结果返回。包括一个main程序，读取从用户购买的物品数量，并显示运费。

def shipping_cost(quantity):
    if quantity <= 0:
        return 0
    return 10.95 + (quantity - 1) * 2.95


if __name__ == '__main__':
    quantity = int(input("请输入购买的商品数量："))
    cost = shipping_cost(quantity)
    print(f"运费是 {cost:.2f} 美元")
