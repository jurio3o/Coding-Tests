def solution(s):
    answer = True
    num_p = 0
    num_y = 0
    for word in s:
        word = word.lower()
        if word == 'p':
            num_p += 1
        elif word == 'y':
            num_y += 1
    if num_p == num_y:
        return True
    else:
        return False