import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    num = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    if num > 1 :    
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for i in range(2,num) :
            dp[0][i] += max(dp[1][i-1],dp[1][i-2])
            dp[1][i] += max(dp[0][i-1],dp[0][i-2])

    print(max(dp[0][num-1],dp[1][num-1]))

# print(*result)