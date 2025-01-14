def solution(s, n):
    answer = ''
    for word in s:
        if word == ' ':
            answer += ' '
        else:
            new_word = ord(word) + n
            if word == word.upper() and new_word > ord('Z'):
                new_word -= 26
            elif word == word.lower() and new_word > ord('z'):
                new_word -= 26
            answer += chr(new_word)
    return answer