def solution(n, lost, reserve):
    answer = n - len(lost)
    lost_res = set(lost) & set(reserve)
    if lost_res:
        answer += len(lost_res)
        for x in lost_res:
            lost.remove(x)
            reserve.remove(x)
    
    for x in sorted(lost):
        if x-1 in reserve:
            reserve.remove(x-1)
            answer += 1
        elif x+1 in reserve:
            reserve.remove(x+1)
            answer += 1
        else:
            pass
    return answer