N, K = map(int, input().split())
word = list(input())
cnt = 0

for n in range(N):
    if word[n] == "P":
        for i in range(n - K, n + K + 1):
            if 0 <= i < N and word[i] == "H":
                word[i] = "-"
                cnt += 1
                break
print(cnt)
        