def solution(n):
    answer = ''
    res = n%2
    num = n//2
    answer = '수박' * num 
    if res: 
        return answer+'수'
    else:
        return answer