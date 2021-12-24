import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

dp = [(0, 0), (scores[0], scores[0])]  # (전 계단 밟음, 전 계단 안 밟음)
for i in range(1, n):
    new = (dp[1][1] + scores[i], max(dp[0]) + scores[i])
    dp = [dp[1], new]

print(max(dp[-1]))

