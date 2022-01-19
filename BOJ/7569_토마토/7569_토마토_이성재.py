from collections import deque
import sys
input = sys.stdin.readline

DELTA = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
]

def bfs():
    global tomato
    queue = deque(ripes)
    day_cnt = 0
    while queue:
        z, y, x, now = queue.popleft()
        day_cnt = max(day_cnt, now)
        tomato -= 1
        for dz, dy, dx in DELTA:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and\
                graph[nz][ny][nx] == '0':
                graph[nz][ny][nx] = '1'
                queue.append((nz, ny, nx, now + 1))

    return day_cnt


m, n, h = map(int, input().split())
graph = [[input().split() for _ in range(n)] for _ in range(h)]

tomato = m * n * h
ripes = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == '1':
                ripes.append((i, j, k, 0))
            elif graph[i][j][k] == '-1':
                tomato -= 1

result = bfs()
if tomato:
    print(-1)
else:
    print(result)