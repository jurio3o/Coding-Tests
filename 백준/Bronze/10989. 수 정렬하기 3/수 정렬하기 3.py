import sys
n = int(input())
result = [0]*10000
for _ in range(n):
    result[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    if result[i] >=1:
        for _ in range(result[i]):
            print(i+1)