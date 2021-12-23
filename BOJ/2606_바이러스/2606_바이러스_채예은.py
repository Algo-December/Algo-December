import sys
input = sys.stdin.readline


def dfs(v):
    global cnt

    cnt += 1
    check[v] = 1

    for x in adj_list[v]:
        if not check[x]:
            dfs(x)


n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]

adj_list = [[] for _ in range(n+1)]  # 1번 ~ n번 컴퓨터 (0은 빈 인덱스)
for edge in edges:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])  # 양방향

check = [0] * (n+1)
cnt = 0
dfs(1)
print(cnt-1)