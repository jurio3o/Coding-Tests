a, b, c = map(int, input().split())
lst = sorted([a,b,c], reverse=True)
if lst[0] >= lst[1] + lst[2]:
    print((lst[1]+lst[2])*2-1)
else:
    print(sum(lst))