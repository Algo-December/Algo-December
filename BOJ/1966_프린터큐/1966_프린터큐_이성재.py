from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    priorities = [(int(num), idx) for idx, num in enumerate(input().split())]  # (우선순위, 인덱스)
    queue = deque(priorities)
    cnt = 0
    while queue:
        num, idx = queue.popleft()
        if queue:
            max_p = max(queue, key=lambda t: t[0])  # 우선순위가 가장 높은 값 찾아냄
            # 현재 숫자보다 우선순위가 높은게 있으면 다시 큐에 삽입
            if max_p[0] > num:
                queue.append((num, idx))

            # 그렇지 않으면 카운트 + 1
            else:
                cnt += 1
                if idx == m:
                    break
        else:
            cnt += 1  

    print(cnt)
