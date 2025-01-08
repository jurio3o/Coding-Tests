def solution(x):
    lst = list(str(x))
    sum_val = sum(int(x) for x in lst)
    answer = x%sum_val
    if answer:
        return False
    else:
        return True