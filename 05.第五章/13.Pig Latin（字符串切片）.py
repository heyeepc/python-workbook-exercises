word = input("输入单词：").lower()

if word[0] in alphabet_Vowel:
    print(word + "way")
else:
    # 找出所有存在于单词中的元音字母的索引位置
    # 比如 "think" 里的 'i' 索引是 2，这里会生成 [2]
    # 如果是 "rhythm"，'y' 索引是 2（假设把 y 算进去）
    vowel_indices = [word.find(v) for v in alphabet_Vowel if v in word]
    
    if vowel_indices:
        # 最小的那个索引，就是第一个元音出现的位置
        first_vowel = min(vowel_indices)
        print(word[first_vowel:] + word[:first_vowel] + "ay")
