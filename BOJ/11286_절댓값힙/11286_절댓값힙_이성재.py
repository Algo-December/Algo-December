from heapq import heappop, heappush
import sys
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
    num = int(input())
    if num > 0:
        heappush(heap, (num, 1))
    elif num < 0:
        heappush(heap, (-num, -1))
    else:
        try:
            a, b = heappop(heap)
            print(a * b)
        except:
            print(0)

