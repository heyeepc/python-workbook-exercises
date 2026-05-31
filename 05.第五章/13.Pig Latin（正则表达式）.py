import re

word = input("输入单词：").lower()

# (^[aeiou]\w*) -> 匹配元音开头的单词
# (^[^aeiouy]+)(\w*) -> 匹配辅音开头（包括y），捕获开头所有的辅音丛，和后面的剩余部分
if re.match(r'^[aeiou]', word):
    print(word + "way")
else:
    # \1 是开头的辅音丛，\2 是后面的部分。把它们调换位置并加 ay
    print(re.sub(r'(^[^aeiouy]+)(\w*)'， r'\2\1ay', word))
