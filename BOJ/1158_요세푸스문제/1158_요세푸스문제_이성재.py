from collections import deque
import sys
input = sys.stdin.readline


# 4000ms, 문제가 하라는대로 따라한다.
n, k = map(int, input().split())
queue = deque(range(1, n + 1))
result = []

while queue:
    # 앞에서 k-1개를 빼서 뒤에 붙이고, k번째 요소를 뺀다.
    for _ in range(k-1):
        num = queue.popleft()
        queue.append(num)
    result.append(queue.popleft())

print(f'<{", ".join(map(str, result))}>')


# 80ms, 인덱스 계산만 해서 해당 인덱스의 요소를 삭제한다.
n, k = map(int, input().split())
numbers = list(range(1, n + 1))
start = 0
result = []
while numbers:
    start += k - 1
    start %= len(numbers)
    result.append(numbers.pop(start))

print(f'<{", ".join(map(str, result))}>')
