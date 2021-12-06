from collections import deque
import sys
input = sys.stdin.readline

# 커서 왼쪽 문자열과 오른쪽 문자열로 나누어 두 개의 덱에 저장
left_chars = deque(input().rstrip())
right_chars = deque()

M = int(input())

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        # 왼쪽 문자열 맨 오른쪽을 오른쪽 문자열로
        if left_chars:
            right_chars.appendleft(left_chars.pop())

    elif cmd[0] == 'D':
        # 오른쪽 문자열 맨 왼쪽을 왼쪽 문자열로
        if right_chars:
            left_chars.append(right_chars.popleft())

    elif cmd[0] == 'B':
        # 왼쪽 문자열 맨 오른쪽 하나 지우기
        if left_chars:
            left_chars.pop()

    elif cmd[0] == 'P':
        # 왼쪽 문자열 맨 오른쪽에 문자 하나 추가
        left_chars.append(cmd[1]) 

print(''.join(left_chars + right_chars))