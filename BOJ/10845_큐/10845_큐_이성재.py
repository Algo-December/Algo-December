import sys
input = sys.stdin.readline

# 단일 연결 리스트를 활용한 큐 구현
class Queue:
    # 연결 리스트를 위한 노드 클래스
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    @property
    def empty(self):
        if self.size > 0:
            return 0
        return 1

    @property
    def front(self):
        if self.size:
            return self.head.data
        return -1

    @property
    def back(self):
        if self.size:
            return self.rear.data
        return -1

    def push(self, X):
        node = self._Node(X)
        if self.empty:
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def pop(self):
        if self.empty:
            return -1
        self.size -= 1
        temp = self.head.data
        self.head = self.head.next
        return temp


queue = Queue()

n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.push(cmd[1])

    elif cmd[0] == 'pop':
        print(queue.pop())

    elif cmd[0] == 'size':
        print(queue.size)

    elif cmd[0] == 'empty':
        print(queue.empty)

    elif cmd[0] == 'front':
        print(queue.front)

    elif cmd[0] == 'back':
        print(queue.back)