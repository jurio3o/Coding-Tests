def solution(num_list):
    even_list = [num for num in num_list if num%2==0 ]
    
    return [len(even_list), len(num_list)-len(even_list)]