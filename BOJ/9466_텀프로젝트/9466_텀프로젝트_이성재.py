import sys
input = sys.stdin.readline

def dfs(start):
    seq = {start: 0}  # key: 정점, value: 탐색 순서
    visited[start] = True
    node = start
    idx = 0
    while True:
        idx += 1
        nxt = graph[node]
        
        if nxt in seq:  # 이번 탐색에 이미 방문한 곳이면
            return idx - seq[nxt]  # nxt부터 시작하는 사이클의 길이

        if visited[nxt]:  # 이전 탐색에 이미 방문한 곳이면
            return 0      # 사이클이 없음

        visited[nxt] = True
        seq[nxt] = idx
        node = nxt
        

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0] + [*map(int, input().split())]
    answer = n
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            answer -= dfs(i)

    print(answer)