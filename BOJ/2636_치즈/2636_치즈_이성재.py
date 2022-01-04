from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    base = [(i, 0) for i in range(n - 1)] +\
            [(n - 1, j) for j in range(m - 1)] +\
            [(i, m - 1) for i in range(1, n)] +\
            [(0, j) for j in range(1, m)]
    queue = deque(base)
    cnt = 0
    while queue:
        base = []
        while queue:
            y, x = queue.popleft()
            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                    visited[ny][nx] = True
                    if graph[ny][nx] == '1':
                        graph[ny][nx] = '0'
                        base.append((ny, nx))
                    else:
                        queue.append((ny, nx))

        cnt += 1
        if base:
            queue = deque(base)
            cheese = len(base)

    return cnt, cheese



n, m = map(int, input().split())
graph = [input().split() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt, cheese = bfs()
print(cnt - 1)
print(cheese)