def solution(n):
    answer = n
    a = format(n, 'b')
    count_a = a.count('1')
    while 1:
        answer += 1
        b = format(answer, 'b')
        count_b = b.count('1')
        if count_a == count_b:  
            break
        
    return answer
