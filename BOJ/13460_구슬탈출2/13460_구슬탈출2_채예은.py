# 1번째 풀이: board를 직접 수정하고 복구하는 버전
import sys
input = sys.stdin.readline


def move(di, dj, red, blue, level):
    global answer
    if level >= answer:
        return

    ri, rj = red
    bi, bj = blue
    nri, nrj = ri, rj
    nbi, nbj = bi, bj

    # 파란구슬
    cnt = 0
    while True:
        nbi += di
        nbj += dj
        if board[nbi][nbj] == 'O':  # 실패
            return
        if board[nbi][nbj] == 'R':
            cnt += 1
        if board[nbi][nbj] == '#':
            for _ in range(cnt+1):
                nbi -= di
                nbj -= dj
            break

    # 빨간구슬
    cnt = 0
    while True:
        nri += di
        nrj += dj
        if board[nri][nrj] == 'O':  # 성공
            answer = min(answer, level)  # 최소값 갱신
            return
        if board[nri][nrj] == 'B':
            cnt += 1
        if board[nri][nrj] == '#':
            for _ in range(cnt + 1):
                nri -= di
                nrj -= dj
            break

    if (bi, bj) == (nbi, nbj) and (ri, rj) == (nri, nrj):
        return

    # 새로운 자리에 구슬 채우기
    board[bi][bj] = '.'
    board[ri][rj] = '.'

    board[nbi][nbj] = 'B'
    board[nri][nrj] = 'R'

    # board[nbi][nbj], board[bi][bj] = board[bi][bj], board[nbi][nbj]
    # board[nri][nrj], board[ri][rj] = board[ri][rj], board[nri][nrj]

    dfs((nri, nrj), (nbi, nbj), level)

    # 복구
    board[nbi][nbj] = '.'
    board[nri][nrj] = '.'

    board[bi][bj] = 'B'
    board[ri][rj] = 'R'

    # board[nbi][nbj], board[bi][bj] = board[bi][bj], board[nbi][nbj]
    # board[nri][nrj], board[ri][rj] = board[ri][rj], board[nri][nrj]
    return


def dfs(red, blue, level):
    if level >= 10:
        return
    move(0, -1, red, blue, level+1)  # 왼쪽
    move(0, 1, red, blue, level+1)  # 오른쪽
    move(-1, 0, red, blue, level+1)  # 위쪽
    move(1, 0, red, blue, level+1)  # 아래쪽


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
        if board[i][j] == 'B':
            blue = (i, j)

answer = float('inf')
dfs(red, blue, 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)

###########################################

# 2번째 풀이: board를 수정하지 않고 R, B 구슬의 위치 정보만 들고다니는 버전
import sys
input = sys.stdin.readline


def move(level, bi, bj, ri, rj, di, dj):
    global answer

    # 파란구슬 이동
    Nbi, Nbj = bi, bj
    cnt = 0
    while board[Nbi][Nbj] != '#':
        Nbi += di
        Nbj += dj
        if board[Nbi][Nbj] == 'O':  # 파란구슬이 구멍을 만나면 실패
            return
        if (Nbi, Nbj) == (ri, rj):  # 빨간구슬
            cnt += 1
    for _ in range(cnt+1):
        Nbi -= di
        Nbj -= dj

    # 빨간구슬 이동
    Nri, Nrj = ri, rj
    cnt = 0
    while board[Nri][Nrj] != '#':
        Nri += di
        Nrj += dj
        if board[Nri][Nrj] == 'O':  # 성공
            answer = min(answer, level)
            return
        if (Nri, Nrj) == (bi, bj):  # 파란구슬
            cnt += 1
    for _ in range(cnt+1):
        Nri -= di
        Nrj -= dj

    if (bi, bj) == (Nbi, Nbj) and (ri, rj) == (Nri, Nrj):  # 이동이 없으면 가지치기
        return

    dfs(level+1, Nbi, Nbj, Nri, Nrj)


def dfs(level, bi, bj, ri, rj):
    if level >= 11:
        return
    if level >= answer:  # 가지치기
        return
    move(level, bi, bj, ri, rj, 0, -1)  # 왼쪽
    move(level, bi, bj, ri, rj, 0, 1)  # 오른쪽
    move(level, bi, bj, ri, rj, -1, 0)  # 위쪽
    move(level, bi, bj, ri, rj, 1, 0)  # 아래쪽


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 빨간구슬, 파란구슬의 좌표를 구하고, .으로 만들기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            ri, rj = i, j
            board[i][j] = '.'
        if board[i][j] == 'B':
            bi, bj = i, j
            board[i][j] = '.'

answer = float('inf')
dfs(1, bi, bj, ri, rj)

if answer == float('inf'):
    print(-1)
else:
    print(answer)