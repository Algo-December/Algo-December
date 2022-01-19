from collections import deque
import sys
input = sys.stdin.readline

DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]
INF = 1e8

def go():
    visited = {(0, 0, True)}
    queue = deque([(0, 0, True, 1, visited)])

    while queue:
        y, x, flag, level, visited = queue.popleft()

        if y == n - 1 and x == m - 1:
            return level

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if (ny, nx, flag) in visited:
                    continue
                
                if graph[ny][nx] == '0':
                    visited.add((ny, nx, flag))
                    queue.append((ny, nx, flag, level + 1, visited))

                elif graph[ny][nx] == '1' and flag:
                    visited.add((ny, nx, False))
                    queue.append((ny, nx, False, level + 1, visited))

    return -1


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
result = go()

if result == INF:
    print(-1)
else:
    print(result)

