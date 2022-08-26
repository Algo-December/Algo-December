import sys
import copy

input = sys.stdin.readline

DELTA = ((0, 1), (1, 0), (0, -1), (-1, 0))


def turn_to_right(i, j, level):
    global matrix
    new_matrix = copy.deepcopy(matrix)
    # 4등분
    si, sj = i, j
    for k in range(4):
        if k == 1:
            si, sj = i, j + 2 ** (level - 1)
        elif k == 2:
            si, sj = i + 2 ** (level - 1), j + 2 ** (level - 1)
        elif k == 3:
            si, sj = i + 2 ** (level - 1), j
        # 블럭 하나 하나
        for bi in range(si, si + 2 ** (level - 1)):
            for bj in range(sj, sj + 2 ** (level - 1)):
                if k == 0:
                    new_matrix[bi][bj + 2 ** (level - 1)] = matrix[bi][bj]
                elif k == 1:
                    new_matrix[bi + 2 ** (level - 1)][bj] = matrix[bi][bj]
                elif k == 2:
                    new_matrix[bi][bj - 2 ** (level - 1)] = matrix[bi][bj]
                elif k == 3:
                    new_matrix[bi - 2 ** (level - 1)][bj] = matrix[bi][bj]
    matrix = new_matrix
    return


def turn(level):
    for i in range(0, 2 ** n, 2 ** level):
        for j in range(0, 2 ** n, 2 ** level):
            # 구역
            turn_to_right(i, j, level)


def melt():
    global matrix
    new_matrix = copy.deepcopy(matrix)
    for i in range(2 ** n):
        for j in range(2 ** n):
            if not matrix[i][j]:
                continue
            cnt = 0
            for di, dj in DELTA:
                ni, nj = i + di, j + dj
                if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and matrix[ni][nj]:
                    cnt += 1
            if cnt < 3:
                new_matrix[i][j] -= 1
    matrix = new_matrix


def dfs(si, sj):
    global max_ice
    stack = [(si, sj)]
    visited[si][sj] = 1
    cnt = 1
    while stack:
        i, j = stack.pop()
        for di, dj in DELTA:
            ni, nj = i + di, j + dj
            if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and matrix[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                stack.append((ni, nj))
                cnt += 1
    max_ice = max(max_ice, cnt)


n, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2 ** n)]
levels = list(map(int, input().split()))

for level in levels:
    if level != 0:
        turn(level)
    melt()

answer = 0
for row in matrix:
    answer += sum(row)

visited = [[0]*2**n for _ in range(2**n)]
max_ice = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if matrix[i][j] and not visited[i][j]:
            dfs(i, j)

print(answer)
print(max_ice)