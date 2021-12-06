import sys
input = sys.stdin.readline

stack = []

n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])

    elif cmd[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)

    elif cmd[0] == 'size':
        print(len(stack))

    elif cmd[0] == 'empty':
        print(int(not stack))

    elif cmd[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    
