def solution(n):

    lst = [int(x) for x in list(str(n))]
    answer = ''
    for x in sorted(lst)[::-1]:
        answer += str(x)
    return int(answer)