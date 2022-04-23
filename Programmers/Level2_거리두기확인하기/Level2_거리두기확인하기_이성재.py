from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 두 칸까지 가보기
def go_two(i, j, place):
    visited = [[False] * 5 for _ in range(5)]
    visited[i][j] = True
    queue = deque([(i, j, 0)])
    
    while queue:
        y, x, cnt = queue.popleft()
        if cnt == 2:
            continue

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                visited[ny][nx] = True
                if place[ny][nx] == 'P':
                    return False
                elif place[ny][nx] == 'O':
                    queue.append((ny, nx, cnt + 1))

    return True

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not go_two(i, j, place):
                    return 0
    return 1


def solution(places):    
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))