import sys
input = sys.stdin.readline

n = int(input())
dp = (0, 0, 0)  # (바로 이전꺼 안먹음 + 이번꺼 먹음, 바로 이전꺼 먹음 + 이번꺼 먹음, 이번 꺼 안먹을래)
for _ in range(n):
    wine = int(input())
    dp = (wine + dp[1], wine + dp[2], max(dp))
    print(dp)
print(max(dp))