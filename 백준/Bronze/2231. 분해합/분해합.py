n = int(input())
lst = []
for num in range(n):
    result = 0
    for i in str(num):
        result += int(i)
    result += num
    if result == n:
        lst.append(num)
if len(lst) == 0:
    print(0)
else:
    print(min(lst))