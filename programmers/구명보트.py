def solution(people, limit):
    answer = 0
    left = 0
    right = len(people)-1
    people.sort(reverse=True)
    
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
        else:
            left +=1
            answer += 1
        if left == right:
            answer += 1
        
    return answer
