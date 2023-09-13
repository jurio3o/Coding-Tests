def solution(food):
    answer = ''
    food_num = 1
    for f in food[1:]:
        num = f//2
        for _ in range(num):
            answer += str(food_num)
        food_num += 1
    answer = answer + '0' + answer[::-1]
    return answer