def solution(hp):
    ant = 0
    for i in [5,3,1]:
        ant += hp//i 
        hp %=i
    return ant