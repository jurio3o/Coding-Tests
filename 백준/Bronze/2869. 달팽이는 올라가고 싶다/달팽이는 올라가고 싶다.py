import math
a, b, v = map(int, input().split())
cnt = math.ceil((v-b)/(a-b))
print(cnt)