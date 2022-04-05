import sys
input = sys.stdin.readline

# 유니온
def union(a, b):
    # 조상을 찾는다.
    a = find(a)
    b = find(b)
    # 조상이 같으면 같은 집합이다.
    if a == b:
        return
    # 조상은 더 큰 녀석으로 정하자.
    if a < b:
        parents[a] = b
    else:
        parents[b] = a

# 파인드, path compression.
def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])  # 재귀적으로 내 조상 찾기. 내 부모는 부모의 부모
    return parents[a]


n, m = map(int, input().split())

parents = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')