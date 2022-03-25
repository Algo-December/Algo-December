import sys, heapq
input = sys.stdin.readline
INF = 1e12
DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dijkstra():
    distances = [[INF] * n for _ in range(n)]
    heap = [(graph[0][0], 0, 0)]
    distances[0][0] = graph[0][0]

    while heap:
        dist, y, x = heapq.heappop(heap)
        
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                nxt_dist = dist + graph[ny][nx]
                if nxt_dist >= distances[ny][nx]:
                    continue
                distances[ny][nx] = nxt_dist
                heapq.heappush(heap, (nxt_dist, ny, nx))

    return distances[-1][-1]

t = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [[*map(int, input().split())] for _ in range(n)]
    result = dijkstra()
    print(f'Problem {t}: {result}')
    t += 1