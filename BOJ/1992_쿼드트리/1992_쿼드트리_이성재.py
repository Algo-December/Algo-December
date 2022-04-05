import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [input().rstrip() for _ in range(n)]

def divide_n_conquer(start, k):
    sy, sx = start
    if k == 1:
        return graph[sy][sx]

    temp = 0
    for i in range(sy, sy + k):
        for j in range(sx,  sx + k):
            temp += int(graph[i][j])

    if temp == 0:
        return '0'
    elif temp == k ** 2:
        return '1'
    
    result = ''
    my, mx = sy + k // 2, sx + k // 2
    result += divide_n_conquer(start, k // 2)
    result += divide_n_conquer((sy, mx), k // 2)
    result += divide_n_conquer((my, sx), k // 2)
    result += divide_n_conquer((my, mx), k // 2)
    return f'({result})'

print(divide_n_conquer((0, 0), n))
      