def solution(nums):
    buff = set(nums) 
    if len(buff) > len(nums)/2:
        return len(nums)/2
    else:
        return len(buff)
