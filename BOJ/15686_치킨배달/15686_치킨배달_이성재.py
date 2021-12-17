from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().split() for _ in range(n)]

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '2':
            chickens.append((i, j))
        elif graph[i][j] == '1':
            houses.append((i, j))

distances = []
for hy, hx in houses:
    distances.append([])
    for cy, cx in chickens:
        now = abs(cy - hy) + abs(cx - hx)
        distances[-1].append(now)

result = 1e10
for comb in combinations(range(len(chickens)), m):
    now = 0
    for d in distances:
        now += min([d[i] for i in comb])

    result = min(result, now)
    if result == m:
        break

print(result)