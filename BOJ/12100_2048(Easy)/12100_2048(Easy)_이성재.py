from copy import deepcopy
import sys

input = sys.stdin.readline


def move_block(matrix, merged, y, x, d):
    dy, dx = DELTA[d]
    num = matrix[y][x]
    for k in range(1, n):
        ny, nx = y + k * dy, x + k * dx
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            matrix[y][x] = 0
            matrix[ny - dy][nx - dx] = num
            return

        if matrix[ny][nx] != 0:
            matrix[y][x] = 0
            if matrix[ny][nx] == num and not merged[ny][nx]:
                merged[ny][nx] = True
                matrix[ny][nx] *= 2
                return

            else:
                matrix[ny - dy][nx - dx] = num
                return


def move_board(matrix, merged, d):
    if d == 0:
        for i in range(1, n):
            for j in range(n):
                if matrix[i][j] != 0:
                    move_block(matrix, merged, i, j, d)
        return

    elif d == 1:
        for i in range(n - 2, -1, -1):
            for j in range(n):
                if matrix[i][j] != 0:
                    move_block(matrix, merged, i, j, d)
        return

    elif d == 2:
        for i in range(n):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    move_block(matrix, merged, i, j, d)
        return

    elif d == 3:
        for i in range(n):
            for j in range(n - 2, -1, -1):
                if matrix[i][j] != 0:
                    move_block(matrix, merged, i, j, d)
        return


def dfs(matrix):
    global answer
    stack = [(matrix, 0)]

    while stack:
        matrix, cnt = stack.pop()
        if cnt == 5:
            for i in range(n):
                for j in range(n):
                    answer = max(answer, matrix[i][j])
            continue

        for d in range(4):
            merged = [[False] * n for _ in range(n)]
            new_matrix = deepcopy(matrix)
            move_board(new_matrix, merged, d)
            stack.append((new_matrix, cnt + 1))


DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(matrix)
print(answer)
