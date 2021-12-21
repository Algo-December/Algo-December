import sys
import copy
input = sys.stdin.readline


def make_comb(level, now):
    if len(now) == m:
        combs.append(copy.deepcopy(now))
        return

    if level == k:
        return

    now.append(level)
    make_comb(level+1, now)
    now.pop()
    make_comb(level+1, now)


n, m = map(int, input().split())  # m: 남겨야하는 치킨집 개수
matrix = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 1:
            houses.append((r, c))
        elif matrix[r][c] == 2:
            chickens.append((r, c))

# 각 집과 치킨집 사이의 거리를 2차원 배열로 저장
# distances[i][j] : i번째 치킨집과 j번째 집 사이 거리
distances = []  # 행: 치킨집 / 열: 집
k = len(chickens)
for i in range(k):
    row = []
    for j in range(len(houses)):
        r1, c1 = houses[j]
        r2, c2 = chickens[i]
        row.append(abs(r1-r2) + abs(c1-c2))
    distances.append(row)

combs = []
make_comb(0, [])  # k개(0~k-1) 중에서 m개를 뽑는 조합

result = float('inf')
for comb in combs:
    cnt = 0
    for h in range(len(houses)):  # 모든 집을 돌면서
        cnt += min(distances[c][h] for c in comb)  # m개의 치킨집까지의 거리들 중 최소값
        if cnt >= result:
            break
    if cnt < result:
        result = cnt

print(result)