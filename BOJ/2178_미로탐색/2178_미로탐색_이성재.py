from collections import deque
import sys
input = sys.stdin.readline

INF = 1e10
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque([(0, 0, 1)])
    distances = [[INF] * m for _ in range(n)]
    while queue:
        y, x, dist = queue.popleft()
        if dist >= distances[y][x]:
            continue
        distances[y][x] = dist
        for d in DELTA:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == '1':
                queue.append((ny, nx, dist + 1))
                
    return distances[-1][-1]

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

print(bfs())