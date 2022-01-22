import sys
input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]

L = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if numbers[j] < numbers[i]:
            L[i] = max(L[i], L[j] + 1)
    if L[i] == 0:
        L[i] = 1
        
print(max(L))