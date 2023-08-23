n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    word_list = []
    string = word[0]
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            string+=word[i+1]
    for w in string:
        if w not in word_list:
            word_list.append(w)
        else:
            cnt+=1
            break
        
print(n-cnt)