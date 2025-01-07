def solution(phone_number):
    length = len(phone_number) - 4
    if not length:
        return phone_number
    else:
        return '*' * length + phone_number[-4:]
