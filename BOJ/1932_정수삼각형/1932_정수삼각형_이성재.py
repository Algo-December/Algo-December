import sys
input = sys.stdin.readline

"""
Idea:

    F(i, j)    F(i, j+1)

        F(i+1, j+1)

=> F(i+1, j+1) = max( F(i, j),  F(i, j+1) ) + s(i, j)
=> F(i, j) : i행 j번째 값을 골랐을 때의 최댓값, s(i, j) : i행 j번째 값
"""

n = int(input())
dp = [int(input())]
for _ in range(n - 1):
    row = list(map(int, input().split()))
    row[0] += dp[0]
    row[-1] += dp[-1]
    for i in range(1, len(row) - 1):
        row[i] += max(dp[i], dp[i - 1])
    dp = row

print(max(dp))
