n = int(input())
ans = 0
for i in range(1,len(str(n))):
    ans += 9*i*10**(i-1)
    
ans += (n - 10**(len(str(n))-1) + 1)*len(str(n))

print(ans)