from itertools import permutations
from collections import deque


def solution(n, weak, dist):
    dist_perms = permutations(dist, len(dist))  # 친구 순서 순열
    min_value = len(dist) + 1
    for dists in dist_perms:
        queue = deque(weak)
        for _ in range(len(weak)):  # 위치 돌리기
            queue.append(queue.popleft() + n)
            i = 0
            j = 0
            now = queue[0]
            while j < len(queue) and i < len(dists):
                # 지금 친구가 갈 수 없는 곳이면, 다음 친구가 다음 약점으로
                if now + dists[i] < queue[j]:
                    i += 1
                    now = queue[j]
                # 지금 친구가 갈 수 있는 곳이면, 다음 약점 확인
                else:
                    j += 1
            min_value = min(min_value, i + 1)

    return min_value if min_value != len(dist) + 1 else -1
