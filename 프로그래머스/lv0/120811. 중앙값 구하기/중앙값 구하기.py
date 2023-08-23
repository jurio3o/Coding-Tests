def solution(array):
    array = sorted(array)
    return array[int((len(array)-1)/2)]