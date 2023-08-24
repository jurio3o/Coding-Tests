def solution(numbers):
    lst=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            lst.append(numbers[i] * numbers[j])
    return max(lst)