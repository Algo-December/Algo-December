import sys
input = sys.stdin.readline

'''
점화식
f(r, c) = max{f(r-1, c-1), f(r-1, c)} + triangle[r][c]
'''


def dp():
    for r in range(1, n):
        for c in range(len(triangle[r])):
            max_up = -1
            for i in range(2):  # 왼쪽 오른쪽 대각선
                if 0 <= c-i < len(triangle[r-1]):
                    max_up = max(max_up, triangle[r-1][c-i])
            triangle[r][c] = triangle[r][c] + max_up

    return max(triangle[n-1])


n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
print(dp())