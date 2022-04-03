import sys
input = sys.stdin.readline

def f(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if matrix[i - 1][j - 1] == '0':
        return 0

    dp[i][j] = min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1
    return dp[i][j]

n, m = map(int, input().split())
matrix = [list(input().rstrip())for _ in range(n)]

dp = [[-1] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 0
    
for i in range(m + 1):
    dp[0][i] = 0


max_result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        max_result = max(max_result, f(i, j))

print(max_result ** 2)

"""
f(i, j) : (i, j)를 맨 오른쪽 아래 꼭짓점으로 하는 가장 큰 정사각형의 길이
f(i, j) = min( f(i-1, j), f(i, j-1), f(i-1, j-1) ) + 1, (i, j)이 1이면.
"""