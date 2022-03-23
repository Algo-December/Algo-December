import sys
input = sys.stdin.readline


'''
시간초과.. 딕셔너리로 풀면 되려나?
'''

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    if x < y:  # 작은 노드를 기준으로 합침
        p[y] = x
    else:
        p[x] = y


for _ in range(int(input())):
    f = int(input())
    name = []
    p = []

    for _ in range(f):
        p1, p2 = input().split()
        if p1 not in name:
            name.append(p1)
            a = len(name)-1
            p.append(a)
        else:
            a = name.index(p1)
        if p2 not in name:
            name.append(p2)
            b = len(name)-1
            p.append(b)
        else:
            b = name.index(p2)

        union(a, b)

        cnt = 0
        for i in range(len(p)):
            if find(i) == 0:
                cnt += 1
        print(cnt)