import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

m, n = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(m)]

dp_matrix = [[-1] * n for _ in range(m)]
dp_matrix[0][0] = 1

def dp(i, j):
    if 0 <= i < m and 0 <= j < n:
        if dp_matrix[i][j] != -1:
            return dp_matrix[i][j]

        dp_matrix[i][j] = 0
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < m and 0 <= nj < n and graph[ni][nj] > graph[i][j]:
                if dp_matrix[ni][nj] == -1:
                    dp_matrix[i][j] += dp(ni, nj)
                else:
                    dp_matrix[i][j] += dp_matrix[ni][nj]

    return dp_matrix[i][j]

print(dp(m - 1, n - 1))
