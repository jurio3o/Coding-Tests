def solution(arr, divisor):
    answer = []
    for x in arr:
        if x%divisor == 0:
            answer.append(x)
            answer = sorted(answer)
    if len(answer) == 0:
        answer.append(-1)
    return answer