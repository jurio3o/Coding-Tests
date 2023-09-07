def solution(k, m, score):
    answer = 0
    box = len(score) // m
    score.sort(reverse=True)
    for i in range(box):
        new_box = score[i*m:(i+1)*m]
        answer += min(new_box)*m
    return answer