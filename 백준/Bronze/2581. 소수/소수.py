m = int(input())
n = int(input())
sosu = []

for x in range(m, n+1):
    error = 0
    if x>1:
        for i in range(2,x):
            if x%i == 0:
                error += 1
        if error == 0:
            sosu.append(x)
if len(sosu):
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)