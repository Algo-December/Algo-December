import sys
input = sys.stdin.readline


def get_candidates(y, x):
    # 빈 칸 (y, x)에 들어갈 수 있는 숫자 후보들 구하는 함수
    result = []
    row = graph[y]
    col = [graph[i][x] for i in range(9)]

    square = set()
    ly, lx = (y // 3) * 3, (x // 3) * 3  # (ly, lx): (y, x)가 포함된 작은 3x3 정사각형의 좌상단 좌표 
    for i in range(ly, ly + 3):
        for j in range(lx, lx + 3):
            square.add(graph[i][j])

    for i in range(1, 10):
        if i in row or i in col or i in square:
            continue
        result.append(i)
    
    return result


def backtrack(level):
    if level == m:
        for row in graph:
            print(' '.join(map(str, row)))
        sys.exit()
        
    now_y, now_x = blanks[level]
    for candidate in get_candidates(now_y, now_x):
        graph[now_y][now_x] = candidate
        backtrack(level + 1)
        graph[now_y][now_x] = 0


graph = [list(map(int, input().split())) for _ in range(9)]

# 빈 칸의 좌표 구하기
blanks = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blanks.append((i, j))

m = len(blanks)
backtrack(0)
