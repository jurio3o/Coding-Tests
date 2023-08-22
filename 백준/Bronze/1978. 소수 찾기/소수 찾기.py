n = int(input())
numbers = map(int, input().split())
cnt = 0
for num in numbers:
    k = 0
    if num!=1:
        for i in range(2,num):
            if num%i != 0:
                k+=1
        if k+2 == num:
            cnt+=1
print(cnt)