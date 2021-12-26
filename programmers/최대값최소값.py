def solution(s):
    answer = ''
    nums = s.split(' ')
    nums.sort(key=int)
    answer = nums[0]+' '+ nums[-1]
    return answer

    # s = list(map(int,s.split()))
    # return str(min(s)) + " " + str(max(s))
