import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    stack = []
    brackets = list(input().rstrip())
    try:
        for bracket in brackets:
            if bracket == '(':
                stack.append(bracket)
            else:
                stack.pop()
        if stack:
            print('NO')
        else:
            print('YES')
    except:
        print('NO')