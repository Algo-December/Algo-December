import sys
input = sys.stdin.readline

def backtrack(level):
    if level == m:
        for row in graph:
            print(' '.join(map(str, row)))
        sys.exit()

    now_y, now_x = blanks[level]
    for num in range(1, 10):
        if not row_cndts[now_y][num]:
            continue
        if not col_cndts[now_x][num]:
            continue
        if not square_cndts[now_y // 3][now_x // 3][num]:
            continue
        
        # 방문 처리
        graph[now_y][now_x] = num
        row_cndts[now_y][num] = False
        col_cndts[now_x][num] = False
        square_cndts[now_y // 3][now_x // 3][num] = False

        backtrack(level + 1)
        
        # 원래대로
        graph[now_y][now_x] = 0
        row_cndts[now_y][num] = True
        col_cndts[now_x][num] = True
        square_cndts[now_y // 3][now_x // 3][num] = True


row_cndts = [[True] * 10 for _ in range(9)]  # row_cndts[i][num]: i행에 num이 올 수 있나요??
col_cndts = [[True] * 10 for _ in range(9)]  # col_cndts[j][num]: j열에 num이 올 수 있나요??
square_cndts = [[[True] * 10 for _ in range(3)] for _ in range(3)]  # square_cndts[i][j][num]: (i, j) 정사각형에 num이 올 수 있나요??

graph = [list(map(int, input().split())) for _ in range(9)]

# 빈 칸의 좌표 구하기
blanks = []
for i in range(9):
    for j in range(9):
        num = graph[i][j]
        if num == 0:
            blanks.append((i, j))
        else:
            row_cndts[i][num] = False
            col_cndts[j][num] = False
            square_cndts[i // 3][j // 3][num] = False

m = len(blanks)
backtrack(0)