import sys
input = sys.stdin.readline

# def dp(i, j):
#     if memo[i][j] != -1:
#         return memo[i][j]

#     if i == j:
#         return 0

#     pres = presum[j + 1] - presum[i]
#     min_result = 1e10
#     for w in range(i, j):
#         min_result = min(min_result, dp(i, w) + dp(w + 1, j))

#         memo[i][j] = min_result  + pres
#     return memo[i][j]


t = int(input())
for _ in range(t):
    k = int(input())
    numbers = [*map(int, input().split())]
    presum = [0]
    for i in range(k):
        presum.append(presum[-1] + numbers[i])


    memo = [[0] * k for _ in range(k)]


    for x in range(1, k):
        for i in range(0, k - x): # 시작점
            j = i + x
            psum = presum[j + 1] - presum[i]
            memo[i][j] = min([memo[i][w] + memo[w+1][j] for w in range(i, j)]) + psum

    print(memo[0][-1])


"""
f[i : j] : (i ~ j 까지 합치는 최소 비용, i ~ j까지 합친 파일 크기)
f[i : j] = (f[i:k][0] + f[k+1:j][0] + f[i:k][1] +f[k+1:j][1]   중 제일 작은 거, i ~ j까지 합친 파일 크기)
"""