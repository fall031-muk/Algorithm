def solution(x):
    answer = True
    buff = 0
    for i in str(x):
        buff += int(i)
    if x % buff == 0:
        answer = True
    else:
        answer = False
    return answer
