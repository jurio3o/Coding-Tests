n = int(input())
stack = []
answer = []
start = 1
possible = True
for _ in range(n):
    num = int(input())
    while start <= num:
        stack.append(start)
        answer.append('+')
        start += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        possible = False
        print('NO')
        break
if possible:
    for i in answer:
        print(i) 