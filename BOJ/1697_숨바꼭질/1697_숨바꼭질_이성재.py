from collections import deque
import sys
input = sys.stdin.readline
INF = 1e10

n, k = map(int, input().split())
visited = [INF] * 100001

queue = deque([(n, 0)])
while queue:
    node, level = queue.popleft()
    if visited[node] <= level:
        continue

    visited[node] = level

    if node == k:
        break

    if node - 1 >= 0:
        queue.append((node - 1, level + 1))

    if 2 * node <= 100000:
        queue.append((2 * node, level + 1))

    if node + 1 <= 100000:
        queue.append((node + 1, level + 1))


print(visited[k])