import sys

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
for i in sorted(lst):
    print(i)