def solution(number, limit, power):
    lst = []
    for i in range(1, number+1):
        num = 0
        for j in range(1, int(i**0.5)+1):
            if i%j==0:
                num += 2
            if i/j == j:
                num -= 1
        lst.append(num)
    answer = []
    for x in lst:
        if x > limit:
            answer.append(power)
        else:
            answer.append(x)
    return sum(answer)