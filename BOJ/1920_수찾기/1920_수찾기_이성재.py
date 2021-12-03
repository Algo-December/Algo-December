import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for b in B:
    print(int(b in A))