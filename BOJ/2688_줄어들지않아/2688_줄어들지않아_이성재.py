import sys
input = sys.stdin.readline

# memo: {key: value}
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


"""
    0  1  2  3  4  5  6  7  8  9
1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  => 10
2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => 55
3: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55] => 220
4: [1, 4, 10, 20, 35, 56, 84, 120, 165, 220] => 715

"""