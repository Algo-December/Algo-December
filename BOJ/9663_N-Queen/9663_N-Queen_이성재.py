import sys
input = sys.stdin.readline

def n_queen(level):
    global answer
    
    # 현재 level 행에서 열 선택
    for i in range(n):
        if col_check[i]:
            continue
        if right_down_check[level - i + n - 1]:
            continue
        if left_down_check[level + i]:
            continue

        if level == n - 1:
            answer += 1
            return

        # 방문 처리
        col_check[i] = 1
        right_down_check[level - i + n - 1] = 1
        left_down_check[level + i] = 1

        n_queen(level + 1)

        # 원래대로
        col_check[i] = 0
        right_down_check[level - i + n - 1] = 0
        left_down_check[level + i] = 0


n = int(input())
answer = 0

col_check = [0] * n  # 열 방문
right_down_check = [0] * (2 * n - 1)  # 오른쪽 아래 대각선, i-j+n-1 = k
left_down_check = [0] * (2 * n - 1)   # 왼쪽 아래 대각선, i+j = k

n_queen(0)
print(answer)