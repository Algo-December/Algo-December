from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = list(input().rstrip())
    n = int(input())
    arr = input()[1:-2]  # 양 옆 괄호 때내기
    arr = arr.split(',') if arr else []  # 빈 문자열이면 빈 리스트 아니면 , 로 스플릿
    queue = deque(arr)
    reversed = False  # 실제로 리스트를 뒤집지 않고 뒤집어진 상태인지만 저장해서 판단
    try:
        for cmd in p:
            if cmd == 'R':
                reversed = not reversed
            elif cmd == 'D':
                if reversed:
                    queue.pop()
                else:
                    queue.popleft()
    except:
        print('error')
        continue

    if reversed and queue:
        queue = list(queue)[::-1]

    print(f'[{",".join(queue)}]')
