import sys

input = sys.stdin.readline
n = int(input())
weights = [int(input()) for _ in range(n)]

weights.sort(reverse=True)

now = 0
for idx, w in enumerate(weights):
    now = max(now, w * (idx + 1))

print(now)