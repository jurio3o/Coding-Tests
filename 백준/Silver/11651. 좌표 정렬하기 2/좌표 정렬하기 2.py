n = int(input())
lst = []
for _ in range(n):
    x,y = map(int, input().split())
    lst.append([y,x])
lst.sort()
for i in range(n):
    print(lst[i][1], lst[i][0])