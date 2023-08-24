n, m = map(int, input().split())
card = list(map(int, input().split()))
lst = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            total = card[i] + card[j] + card[k]
            if m >= total:
                lst.append(total)
print(max(lst))