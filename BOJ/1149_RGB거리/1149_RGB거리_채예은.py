import sys
input = sys.stdin.readline


def dp():
    for r in range(1, n):
        for c in range(3):
            min_up = float('inf')
            for i in range(3):
                if i != c:
                    min_up = min(min_up, matrix[r-1][i])
            matrix[r][c] += min_up
    return min(matrix[-1])


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(dp())