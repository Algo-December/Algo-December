import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = {}
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]

cnt = -1
stack = [1]
visited[1] = True
while stack:
    node = stack.pop()
    cnt += 1

    for nxt in graph.get(node, []):
        if not visited[nxt]:
            visited[nxt] = True
            stack.append(nxt)

print(cnt)