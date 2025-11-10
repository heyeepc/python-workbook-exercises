from collections import Counter

my_list = ['a', 'b', 'c', 'a', 'd', 'b', 'a', 'e', 'c', 'a']

letter_counts = Counter(my_list)

#  打印结果
print(letter_counts)

print(f"'a' 出现的次数: {letter_counts['a']}")

# 获取出现次数最多的 N 个元素
print(letter_counts.most_common(2))
