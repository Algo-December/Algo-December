import sys
input = sys.stdin.readline

# 1) 2차원 테이블 이용


n, k = map(int, input().split())

wv_lst = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    wv_lst.append((w, v))

wv_lst.sort()

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = wv_lst[i]
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[-1][-1])


# 2) 메모리 절약, 시간 단축을 위해 1차원 배열만 사용

n, k = map(int, input().split())

wv_lst = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    wv_lst.append((w, v))

wv_lst.sort()

dp = [0] * (k + 1)
for i in range(1, n + 1):
    w, v = wv_lst[i]
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], v + dp[j - w])

print(dp[-1])