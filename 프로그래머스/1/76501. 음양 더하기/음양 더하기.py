def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            num = abs(num)
        else:
            num = -abs(num)
        answer += num
    return answer