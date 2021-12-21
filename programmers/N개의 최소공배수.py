def solution(arr):
    # 일반적인 최소공배수 풀이
    answer = 0
    a = arr[0]
    for b in arr[1:]:
        for i in range(max(a,b), a*b+1):
            if i%a == 0 and i%b == 0:
                a = i
                break
    answer = a
    return answer
    
    # 유클리드 호제법을 이용한 풀이
#     answer = 0
#     a = arr[0]
#     for b in arr[1:]:
#         multiple = a*b
#         while b:
#             a,b = b, a%b
#             GCD = a
            
#         LCM = multiple/GCD
#         a = LCM
#     answer = a
#     return answer
