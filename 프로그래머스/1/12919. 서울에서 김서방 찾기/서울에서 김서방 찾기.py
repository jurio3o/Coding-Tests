def solution(seoul):
    for i, x in enumerate(seoul):
        if "Kim" == x:
            return f"김서방은 {i}에 있다"