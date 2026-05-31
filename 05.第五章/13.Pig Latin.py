# Pig Latin是通过转化英语单词而构成的一种语言。虽然这种语言的来源是未知的，但它至少在19世纪的两份文件中被提及，表明它已经存在了100多年。将英语翻译成Pig Latin的规则如下：
# 如果单词以辅音字母开头（包括y），那么单词开头的所有字母，直到第一个元音字母（不包括y），都将被删除，然后添加到单词末尾，后面跟着ay。例如，computer 变成omputercay，think 变成inkthay。
# 如果单词以元音开头（不包括y），那么把 way加到单词的末尾。例如，algorithm变成algorithmway，office变成officeway。
# 编写一个程序，从用户那里读取一行文本。然后，程序应该将该行翻译成Pig Latin并显示结果。可以假设用户输入的字符串只包含小写字母和空格。

alphabet_Vowel = ['a', 'e', 'i', 'o', 'u']
alphabet_Consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
word = input("输入单词：")

if word[0] in alphabet_Vowel:
    print(word + "way")
else:
    for i in range(len(word)):
        if word[i] in alphabet_Vowel:
            print(word[i:] + word[:i] + "ay")
            break



