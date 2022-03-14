
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
count_matrix = [[0] * n for _ in range(n)]  # 경우의 수 저장할 dp 2차원 배열
count_matrix[0][0] = 1

def dp(i, j):  # (i, j)까지 가는 경우의 수 반환
    result = 0
    if 0 <= i < n and 0 <= j < n:
        if count_matrix[i][j]:
            return count_matrix[i][j]

        for y in range(0, i):  # 세로줄 검사
            if graph[y][j] + y == i:
                result += dp(y, j)

        for x in range(0, j):  # 가로줄 검사
            if graph[i][x] + x == j:
                result += dp(i, x)

    count_matrix[i][j] = result
    return result

print(dp(n-1, n-1))
