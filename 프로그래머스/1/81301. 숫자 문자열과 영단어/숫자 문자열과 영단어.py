def solution(s):
    
    values = [str(x) for x in list(range(10))]
    keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    dic = dict(zip(keys, values))
    answer = ''
    num_text = ''

    for word in s:
        if word not in values: # word = text
            num_text += word
            try:
                answer += dic[num_text]
                num_text = ''
            except:
                pass
        else: 
            answer += word

    return int(answer)