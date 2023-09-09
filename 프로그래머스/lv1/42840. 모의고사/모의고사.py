def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    length = len(answers)
    
    a = a*(length // len(a))+a[:(length % len(a))]
    b = b*(length // len(b))+b[:(length % len(b))]
    c = c*(length // len(c))+c[:(length % len(c))]
    
    num_a = 0
    num_b = 0
    num_c = 0
    for i, ans in enumerate(answers):
        if ans == a[i]:
            num_a += 1
        if ans == b[i]:
            num_b += 1
        if ans == c[i]:
            num_c += 1


    answer = [num_a,num_b,num_c]
    result = []
    for i, a in enumerate(answer):
        if a == max(answer):
            result.append(i+1)
    return result