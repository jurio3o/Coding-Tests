def solution(arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        lst = []
        for i in range(len(a1)):
            ans = a1[i] + a2[i]
            lst.append(ans)
        answer.append(lst)

    return answer