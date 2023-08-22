n, b = input().split()
num_array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0
n = n[::-1]
for num, i in enumerate(n):
    result += num_array.index(i) * (int(b) ** num)
print(result)