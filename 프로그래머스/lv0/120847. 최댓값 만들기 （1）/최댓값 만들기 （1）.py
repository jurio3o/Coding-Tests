def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    m = numbers[0]
    n = numbers[1]
    return m*n