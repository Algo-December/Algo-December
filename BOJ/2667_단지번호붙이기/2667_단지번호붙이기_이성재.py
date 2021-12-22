import sys
input = sys.stdin.readline

DELTA = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def floodfill(y, x):
    graph[y][x] = '0'
    result[-1] += 1

    for d in DELTA:
        ny = y + d[0]
        nx = x + d[1]

        if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == '1':
            floodfill(ny, nx)



n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            result.append(0)
            floodfill(i, j)

print(len(result))
result.sort()
for r in result:
    print(r)