import sys
input = sys.stdin.readline

'''
점화식
f(n) = min{f(n/3), f(n/2), f(n-1)} + 1  (단 n/3, n/2는 나누어떨어질 때만)
# 동전 거스름돈 문제와 동일
'''


def dp():
    for i in range(2, n+1):
        min_num = float('inf')
        for k in [2, 3]:
            if not i % k:
                ret = memo[i // k]
                min_num = min(min_num, ret)
        min_num = min(min_num, memo[i-1])
        memo[i] = min_num + 1

    return memo[n]


n = int(input())
memo = [0] * (n+1)
print(dp())