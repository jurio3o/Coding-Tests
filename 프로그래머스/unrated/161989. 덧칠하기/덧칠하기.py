def solution(n, m, section):
    start = 0
    cnt = 0
    for s in section:
        if s > start:
            start = (s+m-1)
            cnt += 1
    return cnt