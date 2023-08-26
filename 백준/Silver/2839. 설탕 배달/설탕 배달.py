n = int(input())
z = n // 3
result = []
for a in range(z+1):
    if (n - 3*a) % 5 == 0:
        b = (n - 3*a) // 5 
        result.append(a+b)
if len(result):
    print(min(result))
else:
    print(-1)