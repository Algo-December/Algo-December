DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

def go(graph):
    # 1시간마다 이동
    new_info = {}
    for loc, ameba in graph.items():
        y, x = loc
        num, d = ameba
        ny = y + DELTA[d][0]
        nx = x + DELTA[d][1]
        
        if ny == 0 or nx == 0:  # 상 또는 좌
            num //= 2
            d += 1

        elif ny == n - 1 or nx == n - 1:  # 하 또는 우
            num //= 2
            d -= 1

        new_info[(ny, nx)] = new_info.get((ny, nx), []) + [(num, d)]
    
    return new_info

def merge(graph):
    # 모든 군집이 이동을 마치고 같은 위치에 있는 군집끼리 합침
    for loc, amebas in graph.items():
        # loc에 군집이 여러 개인 경우
        if len(amebas) > 1:
            new_num = sum([ameba[0] for ameba in amebas])
            new_drtn = sorted(amebas, key=lambda x: x[0])[-1][1]  # num이 가장 큰 군집의 방향으로 결정
            graph[loc] = [new_num, new_drtn]

        # loc에 군집이 한 개인 경우
        else:
            graph[loc] = amebas[0]
                    

t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    graph = {}  # key : (y, x) 좌표, value : [미생물 수, 방향]
    for _ in range(k):
        y, x, num, drtn = map(int, input().split())
        graph[(y, x)] = [num, drtn - 1]

    for _ in range(m):
        graph = go(graph)
        merge(graph) 
    
    answer = 0
    for loc, ameba in graph.items():
        answer += ameba[0]        

    print(f'#{tc} {answer}')