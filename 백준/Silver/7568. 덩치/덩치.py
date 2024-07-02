N = int(input())

student = []
for _ in range(N):
    x, y = map(int, input().split())
    student.append([x, y])

for s in student:
    rank = 1
    for s2 in student:
        if s[0] < s2[0] and s[1] < s2[1]:
            rank += 1
    print(rank, end=" ")

            