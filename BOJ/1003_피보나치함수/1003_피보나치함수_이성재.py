import sys
input = sys.stdin.readline
n = int(input())

memo = {0: (1, 0), 1: (0, 1)}
def dp(k):
    if k in memo:
        return memo[k]
    a, b = dp(k - 1)
    c, d = dp(k - 2)
    memo[k] = (a + c, b + d)

    return memo[k]

for _ in range(n):
    k = int(input())
    print(*dp(k))



cache = [(1, 0), (0, 1)]

a = (1, 0)
b = (0, 1)

for _ in range(39):
    temp = (a[0] + b[0], a[1] + b[1])
    a = b
    b = temp
    cache.append(temp)

for _ in range(n):
    k = int(input())
    print(*cache[k])
