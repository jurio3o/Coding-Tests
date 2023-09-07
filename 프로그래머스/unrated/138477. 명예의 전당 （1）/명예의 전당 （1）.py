def solution(k, score):
    answer = []
    lst = []
    for s in score:
        if len(answer)<k:
            lst.append(s)
            answer.append(min(lst))
        else:
            if s >= min(lst):
                lst = sorted(lst)
                lst[0] = s
            else:
                pass
            answer.append(min(lst))
    return answer