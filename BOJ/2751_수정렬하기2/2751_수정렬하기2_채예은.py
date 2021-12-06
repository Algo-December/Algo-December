# n의 범위가 1,000,000이므로 nlogn정렬 X -> 카운팅정렬
import sys
input = sys.stdin.readline

n = int(input())

pos_count = [0] * 1000001  # 0 ~ 1000000
neg_count = [0] * 1000001  # -1 ~ -1000000

for _ in range(n):
    num = int(input())
    if num >= 0:  # 0은 pos_count에서 센다
        pos_count[num] += 1
    else:
        neg_count[abs(num)] += 1

for i in range(1000000, 0, -1):
    if neg_count[i]:
        print(-i)

for j in range(1000001):
    if pos_count[j]:
        print(j)