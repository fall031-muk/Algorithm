# 나의 풀이(3중 for문으로 비효율적)
def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] +number[k] == 0:
                    answer += 1
    return answer


# combinaions를 사용한 풀이
def solution (number) :
    from itertools import combinations
    answer = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            answer += 1
    return answer