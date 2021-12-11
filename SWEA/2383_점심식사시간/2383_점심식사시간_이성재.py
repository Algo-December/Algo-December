# 맨해튼 거리 함수
dist = lambda p, s: abs(p[0] - s[0]) + abs(p[1] - s[1])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    humans = []  # (y좌표, x좌표)
    stairs = []  # (y좌표, x좌표, 계단길이)
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                humans.append((i, j))
            elif graph[i][j] != 0:
                stairs.append((i, j, graph[i][j]))

    k = len(humans)
    result = 1e10
    for i in range(1 << k):
        stair0 = []  # 0번 계단으로 갈 사람 거리
        stair1 = []  # 1번 계단으로 갈 사람 거리
        for j in range(k):
            if (1 << j) & i:  # j번째 사람은 1번 계단
                stair1.append(dist(humans[j], stairs[1]) + 1)
            else:             # j번째 사람은 0번 계단
                stair0.append(dist(humans[j], stairs[0]) + 1)

        stair0.sort()
        stair1.sort()
 
        # (i-3번째 사람이 계단을 모두 내려가는데 걸리는 시간)과 (i번째 사람이 계단까지 도착하는 시간) 비교 
        for i in range(3, len(stair0)):
            stair0[i] = max(stair0[i - 3] + stairs[0][2], stair0[i])

        for i in range(3, len(stair1)):
            stair1[i] = max(stair1[i - 3] + stairs[1][2], stair1[i])
        
        if not stair0:
            temp = stair1[-1] + stairs[1][2]
        elif not stair1:
            temp = stair0[-1] + stairs[0][2]
        else:
            temp = max(stair0[-1] + stairs[0][2], stair1[-1] + stairs[1][2])
        result = min(result, temp)

    print(f'#{tc} {result}')
