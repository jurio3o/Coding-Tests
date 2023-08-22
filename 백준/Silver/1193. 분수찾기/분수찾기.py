x = int(input())
line = 1
while x > line:
    x -= line
    line += 1

if line%2 == 0:
    b = line - x + 1
    a = x
else:
    a = line - x + 1
    b = x
print(a,'/',b, sep='')