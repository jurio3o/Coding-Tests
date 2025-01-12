def solution(s):
    if len(s)%2: #홀수
        idx = len(s)//2
        return s[idx]
    else:
        idx = len(s)//2 - 1
        return s[idx:idx+2]