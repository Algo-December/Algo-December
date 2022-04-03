import sys, heapq
input = sys.stdin.readline
INF = 1e11


def dijkstra(start, graph):
    distances = [INF] * (1 + n)
    heap = [(0, start)]
    distances[start] = 0
    while heap:
        dist, node = heapq.heappop(heap)
        
        for nxt, cost in graph.get(node, []):
            nxt_dist = cost + dist
            if nxt_dist >= distances[nxt]:
                continue
            distances[nxt] = nxt_dist
            heapq.heappush(heap, (nxt_dist, nxt))

    return distances

n, m, x = map(int, input().split())
to_graph = {}
from_graph = {}
for _ in range(m):
    s, e, t = map(int, input().split())
    from_graph[s] = from_graph.get(s, []) + [(e, t)]
    to_graph[e] = to_graph.get(e, []) + [(s, t)]


to_result = dijkstra(x, to_graph)
from_result = dijkstra(x, from_graph)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, to_result[i] + from_result[i])

print(answer)