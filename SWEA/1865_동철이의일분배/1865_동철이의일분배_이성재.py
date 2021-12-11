def backtrack(level, p):
    global max_value
    if level == N:
        max_value = max(max_value, p)
    if p <= max_value:
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        backtrack(level + 1, p * graph[level][i]/100)
        visited[i] = False
    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0
    visited = [False] * N
    backtrack(0, 1)
    print(f'#{tc} {max_value * 100:6f}')