def solution(array, height):
    answer = [arr for arr in array if arr>height]
    return len(answer)