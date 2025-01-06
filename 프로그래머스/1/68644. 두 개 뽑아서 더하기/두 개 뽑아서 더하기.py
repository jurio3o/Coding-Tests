from itertools import combinations

def solution(numbers):
    arr = list(combinations(numbers, 2))
    answer = []
    for x in arr:
        answer.append(sum(x))
    answer = sorted(list(set(answer)))
    return answer