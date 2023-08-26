def solution(numbers, direction):
    result = []
    if direction == 'right':
        result.append(numbers[-1])
        result+=(numbers[0:len(numbers)-1])
    else:
        result+=(numbers[1:len(numbers)])
        result.append(numbers[0])
    return result