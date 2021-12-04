import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

for find in finds:
    if find in A:
        print(1)
    else:
        print(0)
