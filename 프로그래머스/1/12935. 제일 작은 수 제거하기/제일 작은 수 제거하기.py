def solution(arr):
    if len(arr) == 1:
        answer = [-1]
    else:
        min_val = min(arr)
        answer = []
        for i in arr:
            if i != min_val:
                answer.append(i)
    return answer