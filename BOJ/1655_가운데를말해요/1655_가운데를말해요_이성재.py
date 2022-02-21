"""
Idea
1.  중간값보다 작은 값을 보관할 최대 힙(왼쪽 힙)과
    중간값보다 큰 값을 보관할 최소 힙(오른쪽 힙)을 이용한다.

2.  두 힙의 크기는
    왼쪽 힙의 크기 == 오른쪽 힙의 크기 (전체가 짝수개인 경우)이거나
    왼쪽 힙의 크기 + 1 == 오른쪽 힙의 크기 (전체가 홀수개인 경우)이도록 유지한다.

3.  중간값은 언제나 왼쪽 힙의 최댓값이다.
"""

import sys, heapq
input = sys.stdin.readline

n = int(input())
min_heap = [10001]  # 중간값보다 큰 값들
max_heap = [10001]  # 중간값보다 작은 값들

for _ in range(n):
    num = int(input())
    left = -max_heap[0]  # 현재 중간값

    if num <= left:
        heapq.heappush(max_heap, -num)
        if len(min_heap) == len(max_heap) - 2:
            a = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, a)
    else:
        heapq.heappush(min_heap, num) 
        if len(min_heap) > len(max_heap):
            a = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -a)

    print(-max_heap[0])
