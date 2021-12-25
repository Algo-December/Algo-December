import sys
input = sys.stdin.readline

# meme: {key: value}
# value[num] : num으로 끝나는 줄어들지 않는 key자리 수의 개수
memo = {1: [1] * 10,}  

for i in range(2, 65):
    pre = memo[i - 1][:]  # 누적 합
    for j in range(1, 10):
        pre[j] += pre[j - 1]
    memo[i] = pre

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(memo[n]))