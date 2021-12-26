# 재귀함수 풀이
# def solution(n):
#     if n ==0:
#         return 0
#     elif n== 1:
#         return 1
#     return (solution(n-1) + solution(n-2))%1234567

# DP 풀이
def solution(n):
    dp = [None] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]%1234567
