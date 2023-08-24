def solution(my_string):
    word = ''
    for str in my_string:
        if str.islower() : 
            word += str.upper()
        else:
            word += str.lower()
    return word