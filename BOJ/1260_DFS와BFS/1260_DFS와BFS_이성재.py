from collections import deque
import sys
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    visited = [False] * (n + 1)
    result = []
    while stack:
        node = stack.pop()

        if visited[node]:
            continue

        result.append(node)
        visited[node] = True

        for nxt in sorted(graph.get(node, []), reverse=True):
            if visited[nxt]:
                continue
            stack.append(nxt)

    return result

def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    result = []
    while queue:
        node = queue.popleft()

        if visited[node]:
            continue

        result.append(node)
        visited[node] = True

        for nxt in sorted(graph.get(node, [])):
            if visited[nxt]:
                continue
            queue.append(nxt)

    return result

n, m, v = map(int, input().split())
graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]

dfs_result = dfs(v)
bfs_result = bfs(v)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))