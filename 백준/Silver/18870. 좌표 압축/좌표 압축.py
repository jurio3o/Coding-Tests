import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst2 = list(set(lst))
lst2.sort()
result = {}
for i in range(len(lst2)):
    result[lst2[i]] =i
for l in lst:
    print(result[l],end=' ')
