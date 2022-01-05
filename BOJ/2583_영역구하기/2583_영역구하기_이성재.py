import sys
input = sys.stdin.readline


def floodfill(sy, sx):
    result = 0
    stack = [(sy, sx)]
    while stack:
        y, x = stack.pop()

        if graph[y][x]:
            continue

        graph[y][x] = 1
        result += 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 0:
                stack.append((ny, nx))
                

    return result


m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[i][j] = 1

areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            areas.append(floodfill(i, j))
            
print(len(areas))
areas.sort()
print(*areas)
