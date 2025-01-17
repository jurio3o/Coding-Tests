def solution(n):
    numbers = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in numbers:
            numbers -= set(range(i*i, n+1, i))
    return len(numbers)