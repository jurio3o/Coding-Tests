def solution(name, yearning, photo):
    name_dict = dict(zip(name, yearning))
    result = []
    for p in photo:
        score = 0
        for j in p:
            try:
                score += name_dict[j]
            except:
                pass
        result.append(score)
    return result