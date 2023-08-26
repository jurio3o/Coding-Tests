import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

def solution(n):
    answer = lcm(n,6) // 6
    return answer