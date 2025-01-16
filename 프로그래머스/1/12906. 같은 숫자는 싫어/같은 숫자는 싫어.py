def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for x in arr:
        if len(answer):
            if x == answer[-1]:
                pass
            else:
                answer.append(x)
        else:
            answer.append(x)
    return answer