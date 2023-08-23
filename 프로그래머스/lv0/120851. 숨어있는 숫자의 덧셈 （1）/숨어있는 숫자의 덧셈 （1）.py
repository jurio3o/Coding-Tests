def solution(my_string):
    answer=0
    for str in my_string:
        try:
            answer+=int(str)
        except:
            pass
    return answer