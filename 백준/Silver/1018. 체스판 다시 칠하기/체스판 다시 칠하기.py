n, m = map(int, input().split())
board = []
cnt_lst = []
for _ in range(n):
    board.append(input())

for index in range(n-7):
    for row in range(m-7):
        cut_board = board[index:index+8]
        cut_board = [c[row:row+8] for c in cut_board]

        result = ''
        for i, b in enumerate(cut_board):
            if i%2==0:
                result += b
            else:
                result += b[::-1]


        cnt = 0
        for i in range(len(result)):
            if i%2 == 0 and result[i] != 'W':
                cnt += 1
            elif i%2 == 1 and result[i] != 'B':
                cnt += 1
        cnt_lst.append(cnt)

        cnt = 0
        for i in range(len(result)):
            if i%2 == 0 and result[i] != 'B':
                cnt += 1
            elif i%2 == 1 and result[i] != 'W':
                cnt += 1
        cnt_lst.append(cnt)

print(min(cnt_lst))