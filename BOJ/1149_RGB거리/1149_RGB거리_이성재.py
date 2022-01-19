import sys
input = sys.stdin.readline

n = int(input())
dp = tuple(map(int, input().split()))

for _ in range(n - 1):
    costs = list(map(int, input().split()))
    r = costs[0] + min(dp[1], dp[2])
    g = costs[1] + min(dp[0], dp[2])
    b = costs[2] + min(dp[0], dp[1])
    dp = (r, g, b)

print(min(dp))