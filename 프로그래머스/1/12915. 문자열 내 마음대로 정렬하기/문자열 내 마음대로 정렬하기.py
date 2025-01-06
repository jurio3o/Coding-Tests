def solution(strings, n):
    arr = []
    for x in strings:
        ans = x[n] + x
        arr.append(ans)
    answer = []
    for x in sorted(arr):
        answer.append(x[1:])
    return answer