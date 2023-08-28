n = int(input())
word_list = []

for _ in range(n):
    word_list.append(input())
word_list = list(set(word_list))
result = []
for l in range(1,max([len(word) for word in word_list])+1):
    len_word = [word for word in word_list if len(word) == l]
    len_word.sort()
    result+=(len_word)
for r in result:
    print(r)