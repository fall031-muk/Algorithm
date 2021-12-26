def solution(n):
    answer = 0
    count = 0
    num = 1
    for i in range(1, n+1):
        for j in range(i, n+1):
            answer += j
            if answer == n:
                count += 1
                
            elif answer > n:
                break
        answer = 0
            
    return count
