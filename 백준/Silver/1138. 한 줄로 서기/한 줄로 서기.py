N = int(input())
num_list = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if result[j] == 0 and num_list[i] == cnt:
            result[j] = i+1
            break
        elif result[j] == 0:
            cnt += 1
            
print(*result)