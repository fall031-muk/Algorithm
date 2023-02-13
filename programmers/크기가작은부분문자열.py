def solution(t, p):
    answer = 0
    p_size = len(p)
    for i in range(len(t)-(p_size-1)):
        if t[i:i+p_size] <= p:
            answer += 1
    return answer