def is_sorted_all(list_1):
    # list_1[:-1] 是去掉最后一个元素的列表
    # list_1[1:]  是去掉第一个元素的列表
    # zip 相当于把相邻的两个数打包在一起，比如 (1, 2), (2, 3)
    
    # 检查是否全部满足升序
    inc = all(x <= y for x, y in zip(list_1[:-1], list_1[1:]))
    # 检查是否全部满足降序
    dec = all(x >= y for x, y in zip(list_1[:-1], list_1[1:]))
    
    return inc or dec
