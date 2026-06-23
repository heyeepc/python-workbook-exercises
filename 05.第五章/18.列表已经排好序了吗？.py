# 编写一个函数，来确定值列表是否按顺序排序（升序或降序）。如果列表已经排序，函数应该返回 True，否则应该返回False。编写一个main程序，从用户那里读取一个数字列表，然后使用函数报告这个列表是否已排序。
def Ascending_descending(list_1):

    if list_1 == sorted(list_1):
        return True
    if list_1 == sorted(list_1, reverse=True):
        return True
    else:
        return False

if __name__ == '__main__':

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    c = [3,5,9,5,0]

    print(Ascending_descending(a))
    print(Ascending_descending(b))
    print(Ascending_descending(c))
