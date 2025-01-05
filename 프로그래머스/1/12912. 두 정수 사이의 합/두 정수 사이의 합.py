def solution(a, b):
    if a == b:
        return a
    else:
        length = abs(b-a) + 1
        answer = length * (a + b) / 2
        return answer