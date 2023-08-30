import sys
word = list(input())
word2 = []
m = int(input())
index = len(word)
for _ in range(m):
    order = list(sys.stdin.readline().split())
    if order[0] == "L" and len(word):
        word2.append(word.pop())
    elif order[0] == "D" and len(word2):
        word.append(word2.pop())
    elif order[0] == "B" and len(word):
        word.pop()
    elif order[0] == "P":
        word.append(order[1])
print(''.join(word + list(reversed(word2))))