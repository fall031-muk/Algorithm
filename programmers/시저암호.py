def solution(s, n):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    answer = ''
    for i in range(len(s)):
        if s[i] in upper:
            answer+=upper[(upper.find(s[i]) + n)%26]
        elif s[i] in lower:
            answer+=lower[(lower.find(s[i]) + n)%26]
        else:
            answer+=" "
    return answer
