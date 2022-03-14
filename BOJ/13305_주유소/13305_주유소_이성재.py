import sys
input = sys.stdin.readline

n = int(input())
roads = [*map(int, input().split())]
gas = [*map(int, input().split())]

for i in range(n - 1):
    if gas[i] < gas[i + 1]:
        gas[i + 1] = gas[i]

print(sum([roads[i] * gas[i] for i in range(n - 1)]))
