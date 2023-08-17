word = []
length = []
for i in range(5):
    input_word = input()
    word.append(input_word)
    length.append(len(input_word))


for col in range(15):
    for row in range(5):
        if col < length[row]:
            print(word[row][col], end ='')
