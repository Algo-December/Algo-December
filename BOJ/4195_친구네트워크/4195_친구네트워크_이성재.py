import sys
input = sys.stdin.readline

# 파인드, path compression
def find(name):
    if parents[name] != name:
        parents[name] = find(parents[name])
    return parents[name]

# 유니온 by rank
def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    rank[a] = rank.get(a, 0)
    rank[b] = rank.get(b, 0)

    # rank가 더 낮은 애한테 붙이자. => 트리의 높이를 최소화 하자.
    if rank[a] > rank[b]:
        parents[a] = b
    else:
        parents[b] = a
        if rank[a] == rank[b]:
            rank[b] += 1

    # 집합 사이즈 측정
    size[a] = size.get(a, 1)
    size[b] = size.get(b, 1)
    size[a], size[b] = size[a] + size[b], size[a] + size[b]


t = int(input())
for _ in range(t):
    parents = {}  # 이름 별로 부모 저장을 위해 딕셔너리 사용
    rank = {}
    size = {}
    f = int(input())
    for _ in range(f):
        a, b = input().split()
        parents[a] = parents.get(a, a)  # KeyError를 막기 위해 get으로
        parents[b] = parents.get(b, b)

        union(a, b)

        print(size[parents[a]])  # 집합의 크기 출력
