s = input()
alphabet = [-1] * 26
num = 0
for i in s:
    num +=1
    if alphabet[ord(i)-97] == -1:
        alphabet[ord(i)-97] += num
print(*alphabet)