import sys
input = sys.stdin.readline

pos_nums = [False] * 1000001  # 0 ~ 1,000,000
neg_nums = [False] * 1000001  # -1 ~ -1,000,000

n = int(input())
for _ in range(n):
    a = int(input())
    if a >= 0:
        pos_nums[a] = True
    else:
        neg_nums[-a] = True

for i in range(1000000, -1, -1):
    if neg_nums[i]:
        print(-i)

for i in range(1000001):
    if pos_nums[i]:
        print(i)