# DP, top-down
import sys
input = sys.stdin.readline

memo = {1: 1, 2: 2, 3: 4}

def dp(k):
    if k in memo:
        return memo[k]
    memo[k] = dp(k - 3) + dp(k - 2) + dp(k - 1)
    return memo[k]

T = int(input())
for _ in range(T):
    print(dp(int(input())))



# DP 다른 풀이, bottom-up
a, b, c = 1, 2, 4

result = [1, 2, 4]
for _ in range(4, 12):
    d = a + b + c
    result.append(d)
    a = b
    b = c
    c = d

T = int(input())
for _ in range(T):
    print(result[int(input()) - 1])



