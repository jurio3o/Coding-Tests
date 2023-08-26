n = int(input())
num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)
for i in sorted(num_list):
    print(i)