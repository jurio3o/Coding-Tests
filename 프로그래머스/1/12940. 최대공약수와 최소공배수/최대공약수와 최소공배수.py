from math import gcd
def solution(n, m):
    answer=[]
    gcd_value = gcd(n,m)
    lcm_value = n*m//gcd(n,m)
    answer.append(gcd_value)
    answer.append(lcm_value)
    return answer