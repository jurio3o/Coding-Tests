n = int(input())
lst = [i for i in str(n)]
lst.sort(reverse=True)
print(int(''.join(lst)))