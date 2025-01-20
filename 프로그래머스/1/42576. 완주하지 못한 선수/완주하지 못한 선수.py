from collections import Counter
def solution(participant, completion):
    answer = ''
    count_dict = dict(Counter(participant))
    for x in completion:
        count_dict[x] -= 1

    for key, value in count_dict.items():
        if value:
            answer += key
    return answer