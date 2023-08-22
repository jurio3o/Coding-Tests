n, b = map(int, input().split())
num_array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''
while n:
    result += num_array[n%b]
    n //= b
print(result[::-1])