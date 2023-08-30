def solution(t, p):
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        num_t = int(t[i:i+len(p)])
        if num_t <= int(p):
            answer += 1
    return answer