import sys
input = sys.stdin.readline

class MyHeap:
    def __init__(self):
        self.tree = []

    def push(self, data):
        self.tree.append(data)
        i = len(self.tree) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.tree[parent] < data:
                self.tree[parent], self.tree[i] = data, self.tree[parent]
                i = parent
            else:
                break

    def pop(self):
        if not self.tree:
            return 0
        root = self.tree[0]
        self.tree[0] = self.tree[-1]
        self.tree.pop()
        last = len(self.tree)
        i = 0
        while i < last:
            child = 2 * i + 1
            if child + 1 < last and self.tree[child] < self.tree[child + 1]:
                child += 1

            if child >= last or self.tree[i] >= self.tree[child]:
                break

            self.tree[i], self.tree[child] = self.tree[child], self.tree[i]
            i = child

        return root

heap = MyHeap()

n = int(input())
for _ in range(n):
    a = int(input())
    if a:
        heap.push(a)
    else:
        print(heap.pop())