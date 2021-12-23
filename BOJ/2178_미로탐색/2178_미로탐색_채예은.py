import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((0, 0, 1))  # 시작점(0, 0) q에 추가
    check[0][0] = 1

    while q:
        x, y, cnt = q.popleft()

        for dr, dc in DIRECTION:
            nr, nc = x + dr, y + dc

            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == '1' and not check[nr][nc]:
                check[nr][nc] = 1
                q.append((nr, nc, cnt+1))

                if nr == n-1 and nc == m-1:  # 도착점 (n-1, m-1)
                    print(cnt+1)
                    return


n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
check = [[0]*m for _ in range(n)]
DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))

bfs()