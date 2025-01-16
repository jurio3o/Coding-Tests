def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1):
        a = n//i
        b = n/i
        if a == b:
            if a != i:
                answer += a
                answer += i
            else:
                answer += i
        
    return answer