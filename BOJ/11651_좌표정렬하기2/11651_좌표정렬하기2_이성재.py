import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort(key=lambda point:(point[1], point[0]))
for point in points:
    print(f'{point[0]} {point[1]}')