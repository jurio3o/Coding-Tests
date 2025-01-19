from collections import Counter
def solution(X, Y):
    answer = ''
    x = Counter(sorted(list(X), reverse=True))
    y = Counter(sorted(list(Y), reverse=True))

    dic = dict(x&y)

    if len(dic)==0:
        return '-1'
    
    for key, value in dict(x&y).items():
        answer += key*value

    if set(answer) == {'0'}:
        return '0'
    else:
        return answer