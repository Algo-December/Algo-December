from collections import deque
import sys
input = sys.stdin.readline

DELTA = [(1, 0), (0, -1), (0, 1), (-1, 0)]
def bfs():
    queue = deque(ripes)
    cnt = 0
    while queue:
        y, x, now = queue.popleft()
        cnt = max(cnt, now)
        for dy, dx in DELTA:
            ny, nx = dy + y, dx + x
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == '0':
                graph[ny][nx] = '1'
                queue.append((ny, nx, now + 1))

    return cnt

m, n = map(int, input().split())
graph = [list(input().split()) for _ in range(n)]
ripes = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            ripes.append((i, j, 0))

result = bfs()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            result = -1

print(result)