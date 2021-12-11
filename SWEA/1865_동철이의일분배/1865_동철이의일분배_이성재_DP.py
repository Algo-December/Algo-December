def dp(i, j):  # i번째 사람에게 일을 줄건데, 지금 이미 고른 일들은 j임. 최댓값을 알려줘. 라는 함수
    if i == N:
        return 1

    if memo[i][j] != -1:
        return memo[i][j]
    
    result = 0
    for k in range(N):
        # 아직 k번째 일을 안 골랐다면
        if (1 << k) & j == 0:
            result = max(result, dp(i + 1, j | (1 << k)) * graph[i][k] / 100) 
    
    memo[i][j] = result
    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1] * (1 << N) for _ in range(N)]  # dp(i, j) 결과값 저장 배열, 메모이제이션
    print(f'#{tc} {dp(0, 0) * 100:.6f}')
