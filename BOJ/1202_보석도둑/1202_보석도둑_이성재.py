"""
Idea:
가벼운 가방 순서대로,
가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석을 찾기.
"""
import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
answer = 0
jewels = sorted([tuple(map(int, input().split())) for _ in range(n)])  # 무게가 작고, 가치가 작은 순서

bags = sorted([int(input()) for _ in range(k)])
i = 0  # 보석 인덱스
heap = []
for bag in bags:
    # 현재 가방에 넣을 수 있는 보석들을 모두 최대 힙에
    while i < n and jewels[i][0] <= bag:
        heapq.heappush(heap, -jewels[i][1])  # 가치 최대 힙
        i += 1
    # 가장 가치가 높은 보석을 현재 가방에 담음.
    if heap:
        value = -heapq.heappop(heap)
        answer += value

print(answer)

