import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0]
for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)
        
coins.sort()
n = len(coins) - 1

dp = [1] + [0] * (k)

for i in range(1, n + 1):
    coin = coins[i]
    for j in range(1, k + 1):
        if j >= coin:
            dp[j] += dp[j - coin]
        

print(dp[-1])

