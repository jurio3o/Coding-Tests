def solution(d, budget):
    answer = 0
    for x in sorted(d):
        if budget-x<0:
            break
        budget -= x
        answer += 1
    return answer