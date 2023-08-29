t = int(input())
for _ in range(t):
    result = list(input().split())
    for i in range(len(result)):
        print(result[i][::-1], end = ' ')