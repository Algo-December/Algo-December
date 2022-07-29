import sys

input = sys.stdin.readline


def roll(d):
    global y, x
    dy, dx = DELTA[d]
    ny, nx = y + dy, x + dx
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        return

    # 동
    if d == 1:
        dice[0], dice[4], dice[2], dice[5] = dice[4], dice[2], dice[5], dice[0]

    # 서
    elif d == 2:
        dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]

    # 북
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

    # 남
    elif d == 4:
        dice[0], dice[3], dice[2], dice[1] = dice[3], dice[2], dice[1], dice[0]

    if matrix[ny][nx] == 0:
        matrix[ny][nx] = dice[2]
    else:
        dice[2] = matrix[ny][nx]
        matrix[ny][nx] = 0

    y, x = ny, nx
    print(dice[0])


DELTA = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]

n, m, y, x, k = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
commands = [*map(int, input().split())]

dice = [0, 0, 0, 0, 0, 0]  # 위, 앞, 밑, 뒤, 왼, 오

for cmd in commands:
    roll(cmd)
