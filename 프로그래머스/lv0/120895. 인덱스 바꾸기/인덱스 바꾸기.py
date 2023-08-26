def solution(my_string, num1, num2):
    a = my_string[num1]
    b = my_string[num2]
    my_string = my_string[:num1] + b + my_string[num1+1:num2] + a + my_string[num2+1:]
    return my_string