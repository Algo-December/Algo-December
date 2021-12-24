import sys
n = int(sys.stdin.readline())

INF = 1e10

# memo = [INF] * 1000001
# memo[1] = 0

# for now in range(1, 1000001):
#     for nxt in [2 * now, 3 * now, now + 1]:
#         if nxt > 1000000:
#             continue
#         memo[nxt] = min(memo[now] + 1, memo[nxt])

# print(memo[n])

"""
Idea : 
F(k) = min ( 
    F(k - 1), 
    F(k // 2),   (if k%2 == 0) 
    F(k // 3)    (if k%3 == 0) 
    )
    + 1
"""


memo = [INF] * (n + 1)
memo[1] = 0
for k in range(2, n + 1):
    result = [memo[k], memo[k - 1] + 1]
    if k % 2 == 0:
        result.append(memo[k // 2] + 1)
    if k % 3 == 0:
        result.append(memo[k // 3] + 1)
    
    memo[k] = min(result)

print(memo[n])
