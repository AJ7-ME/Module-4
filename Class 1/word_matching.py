def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words that start and end with the same letter:", lst)
    return ctr
count = match_words(['abc', 'cfa', 'xyx', 'aba', '1221', 'hello', 'world', 'level', 'bob', 'mom', 'dad', 'sis'])
print("Number of words that start and end with the same letter:", count)