n, m = map(int, input().split())
basket = list(range(1,n+1))
for _ in range(m):
    i, j = map(int, input().split())
    a = basket[i-1]
    b = basket[j-1]
    basket[i-1] = b
    basket[j-1] = a
for num in range(n):
    print(basket[num], end =' ')