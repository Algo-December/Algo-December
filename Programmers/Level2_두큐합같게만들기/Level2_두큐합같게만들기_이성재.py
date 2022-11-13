from collections import deque


def solution(queue1, queue2):
    n = len(queue1)

    left = sum(queue1)
    right = sum(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    for cnt in range(3 * n):
        if left < right:
            num = queue2.popleft()
            queue1.append(num)
            left += num
            right -= num

        elif left > right:
            num = queue1.popleft()
            queue2.append(num)
            left -= num
            right += num
        else:
            return cnt

    return -1
