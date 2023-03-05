def solution(s):
    answer = []
    buff = ''
    for c in s:
        if c not in buff:
            answer.append(buff.rfind(c))
        else:
            answer.append(len(buff) - buff.rfind(c))
        buff+=c
    return answer