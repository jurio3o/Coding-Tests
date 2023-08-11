n, m = map(int, input().split())
basket = list(range(1,n+1))

for _ in range(m):
    i, j = map(int, input().split())
    reverse_list = basket[i-1:j]
    reverse_list.reverse()
    basket[i-1:j] = reverse_list
for i in range(n):
    print(basket[i], end = ' ')