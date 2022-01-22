from sched import scheduler
import sys
input = sys.stdin.readline

n = int(input())

schedules = []
for _ in range(n):
    s, e = map(int, input().split())
    schedules.append((s, e))

schedules.sort(key=lambda arr: (arr[1], arr[0]))

result = 0
now = 0
for s, e in schedules:
    if now <= s:
        now = e
        result += 1

print(result)