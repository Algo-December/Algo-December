import sys, heapq
input = sys.stdin.readline
INF = 1e12

def dijkstra(start):
    distances = [INF] * (1 + v)
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        for nxt_node, nxt_cost in graph[node]:
            dist = nxt_cost + cost
            if dist >= distances[nxt_node]:
                continue
            distances[nxt_node] = dist
            heapq.heappush(heap, (dist, nxt_node))

    return distances


v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = dijkstra(k)

for r in result[1:]:
    if r == INF:
        print('INF')
    else:
        print(r)