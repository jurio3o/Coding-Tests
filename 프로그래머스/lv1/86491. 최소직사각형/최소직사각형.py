def solution(sizes):
    result = [0,0]
    for size in sizes:
        size.sort(reverse=True)
        if size[0] >= result[0]:
            result[0] = size[0]
        if size[1] >= result[1]:
            result[1] = size[1]

    return result[0]*result[1]