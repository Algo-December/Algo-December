import bisect
n = int(input())
numbers = [*map(int, input().split())]

L = [numbers[0]]
for i in range(1, n):
    num = numbers[i]
    if num <= L[-1]:
        idx = bisect.bisect_left(L, num)
        L[idx] = num
    else:
        L.append(num)

print(len(L))