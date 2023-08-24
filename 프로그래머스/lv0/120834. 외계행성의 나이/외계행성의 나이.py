def solution(age):
    answer = ""
    lst = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    for a in str(age):
        answer += lst[int(a)]
    return answer