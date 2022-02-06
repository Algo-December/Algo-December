import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a:
        heapq.heappush(heap, a)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)




# 최소 힙 구현
class MinHeap:
    def __init__(self):
        self.tree = []  # 완전 이진 트리
        
    # 삽입 연산
    def push(self, data):
        self.tree.append(data)
        i = len(self.tree) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.tree[parent] > data:
                self.tree[i] = self.tree[parent]
                self.tree[parent] = data
                i = parent
            else:
                break

    # 삭제 연산
    def pop(self):
        if not self.tree:
            return 0
        root = self.tree[0]
        self.tree[0] = self.tree[-1]  # 마지막 원소를 루트 노드로
        self.tree.pop()  # 마지막 원소 제거
        last = len(self.tree)
        i = 0
        while i < last:
            child = 2 * i + 1  # 왼쪽 자식
            # 왼쪽 자식이 더 작으면 왼쪽 자식을 이용
            if child + 1 < last and self.tree[child] > self.tree[child + 1]:
                child += 1

            # 범위를 넘어갔거나, 부모보다 크면 break
            if child >= last or self.tree[i] <= self.tree[child]:
                break

            self.tree[i], self.tree[child] = self.tree[child], self.tree[i]
            i = child

        return root




n = int(input())
my_heap = MinHeap()
for _ in range(n):
    a = int(input())
    if a:
        my_heap.push(a)
    else:
        print(my_heap.pop())