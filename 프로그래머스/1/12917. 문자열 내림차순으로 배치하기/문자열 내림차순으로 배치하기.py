def solution(s):
    answer = ''
    lst = sorted([ord(x) for x in s])[::-1]
    for x in lst:
        answer += chr(x)
    return answer