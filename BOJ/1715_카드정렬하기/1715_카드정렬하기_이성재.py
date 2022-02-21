import sys, heapq
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    heapq.heappush(heap, int(input()))

answer = 0
while len(heap) > 1:
    a = heapq.heappop(heap)    # 현재 카드 더미 중 가장 적은 2개 고르기
    b = heapq.heappop(heap)
    now = a + b                # 새로운 카드 더미
    heapq.heappush(heap, now)
    answer += now              # 새로운 카드 더미를 만드는데 걸리는 비교 횟수

print(answer)