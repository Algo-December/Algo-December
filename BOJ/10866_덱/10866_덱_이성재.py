import sys
input = sys.stdin.readline

# 이중 연결 리스트를 활용한 Double-Ended 큐 구현
class Deque:

    # 이중 연결 리스트를 위한 노드 클래스
    class _Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

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

    def push_front(self, X):
        node = self._Node(X)
        if self.empty:
            self.head = node
            self.rear = node
        else:
            node.right = self.head
            self.head.left = node
            self.head = node
        self.size += 1

    def push_back(self, X):
        node = self._Node(X)
        if self.empty:
            self.head = node
            self.rear = node
        else:
            node.left = self.rear
            self.rear.right = node
            self.rear = node
            
        self.size += 1

    def pop_front(self):
        if self.empty:
            return -1
        self.size -= 1
        temp = self.head.data
        self.head = self.head.right
        return temp

    def pop_back(self):
        if self.empty:
            return -1
        self.size -= 1
        temp = self.rear.data
        self.rear = self.rear.left
        return temp


queue = Deque()

n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        queue.push_front(cmd[1])

    elif cmd[0] == 'push_back':
        queue.push_back(cmd[1])

    elif cmd[0] == 'pop_front':
        print(queue.pop_front())

    elif cmd[0] == 'pop_back':
        print(queue.pop_back())

    elif cmd[0] == 'size':
        print(queue.size)

    elif cmd[0] == 'empty':
        print(queue.empty)

    elif cmd[0] == 'front':
        print(queue.front)

    elif cmd[0] == 'back':
        print(queue.back)
