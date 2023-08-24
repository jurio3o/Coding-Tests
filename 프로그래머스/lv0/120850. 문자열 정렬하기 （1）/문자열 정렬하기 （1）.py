def solution(my_string):
    lst = []
    for str in my_string:
        try:
            lst.append(int(str))
        except:
            pass
    lst = sorted(lst)
    return lst