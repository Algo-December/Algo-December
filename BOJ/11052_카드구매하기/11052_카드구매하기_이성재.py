import sys
input = sys.stdin.readline

n = int(input())
numbers = [0] + [*map(int, input().split())]

dp = [[i for i in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j >= i:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - i] + numbers[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
