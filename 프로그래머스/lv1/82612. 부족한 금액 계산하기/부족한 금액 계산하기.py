def solution(price, money, count):
    num = 0
    for i in range(1,count+1):
        num += i
    answer = num * price - money
    if answer>= 1:
        return answer
    else:
        return 0