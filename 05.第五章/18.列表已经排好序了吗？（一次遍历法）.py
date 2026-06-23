def is_sorted_one_pass(list_1):
    if len(list_1) <= 1:
        return True

    is_ascending = True
    is_descending = True

    # 只遍历一次列表
    for i in range(len(list_1) - 1):
        if list_1[i] > list_1[i + 1]:
            is_ascending = False  # 出现前数大于后数，不是升序
        if list_1[i] < list_1[i + 1]:
            is_descending = False  # 出现前数小于后数，不是降序

        # 如果既不是升序也不是降序，提前结束循环（剪枝优化）
        if not is_ascending and not is_descending:
            return False

    return is_ascending or is_descending
