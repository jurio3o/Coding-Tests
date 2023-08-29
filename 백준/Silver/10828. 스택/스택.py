import sys
x = int(input())
stack = []
for _ in range(x):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif order[0] == 'pop':
        if len(stack):
            print(stack.pop())

        else:
            print(-1)