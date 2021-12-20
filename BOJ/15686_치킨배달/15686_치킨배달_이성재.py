from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().split() for _ in range(n)]

# 집과 치킨집의 좌표 저장
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '2':
            chickens.append((i, j))
        elif graph[i][j] == '1':
            houses.append((i, j))

# 각 집과 치킨집 사이의 거리를 2차원 배열로 저장
# distances[i][j] : i번째 가정집과 j번째 치킨집 사이 거리
distances = []
for hy, hx in houses:
    distances.append([])
    for cy, cx in chickens:
        now = abs(cy - hy) + abs(cx - hx)
        distances[-1].append(now)

result = 1e10
for comb in combinations(range(len(chickens)), m):
    now = 0
    for d in distances:  # d: 한 가정집의 치킨집들까지의 거리 배열
        now += min([d[i] for i in comb])  # 고른 m개의 치킨집까지의 거리들 중 최솟값

    result = min(result, now)
    if result == m:
        break

print(result)