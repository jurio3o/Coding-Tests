import sys
input = sys.stdin.readline

def func(x):
    if x == 1:
        return 1
    elif x == 2: 
        return 2
    elif x == 3:
        return 4
    else:
        return func(x-3) + func(x-2) + func(x-1)
T = int(input())
for _ in range(T):
    N = int(input())
    print(func(N))
 