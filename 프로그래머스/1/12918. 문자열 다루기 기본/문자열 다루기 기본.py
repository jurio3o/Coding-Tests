def solution(s):
    if len(s) in [4,6]:
        try:
            int(s)
            return True
        except:
            pass
    return False
        