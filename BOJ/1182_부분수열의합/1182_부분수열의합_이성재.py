# 4300ms, 비트마스킹 활용, 브루트포스
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

cnt = 0
for i in range(1, 1 << n):
    result = 0
    for j in range(n):
        if i & (1 << j):
            result += numbers[j]
    if result == s:
        cnt += 1

print(cnt)


# 500ms, combinations 활용, 브루트 포스
from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
for start_idx in range(n):  # 몇번째 숫자부터 더할건지
    for cnt in range(n - start_idx):  # 몇 개의 숫자를 더할 건지
        combs = combinations(numbers[start_idx + 1:], cnt)  # 뽑는다.
        for num_tuple in combs:
            total = numbers[start_idx] + sum(num_tuple)
            if total == s:
                answer += 1
print(answer)