def solution(dartResult):
    dart = list(dartResult)
    if '10' in dartResult:
        for i, x in enumerate(dart):
            if x == '1' and dart[i+1] == '0':
                dart[i] = '10'
                dart.pop(i+1)
    
    lst = []
    num_cnt = -1
    for idx, x in enumerate(dart):
        if x.isdigit():
            lst.append(int(x))
            num_cnt += 1
        elif x=='S':
            lst[num_cnt] = lst[num_cnt]**1
        elif x=='D':
            lst[num_cnt] = lst[num_cnt]**2
        elif x=='T':
            lst[num_cnt] = lst[num_cnt]**3
        elif x=='*':
            lst[num_cnt] = lst[num_cnt]*2
            if num_cnt:
                lst[num_cnt-1] = lst[num_cnt-1]*2
        elif x=='#':
            lst[num_cnt] = -lst[num_cnt]
    return sum(lst)