n = int(input())

def move(n, A, B, C):
    # A에 있는 n개의 원판을 C로 옮김.
    if n == 1:
        print(A, C)
        return
    move(n - 1, A, C, B)
    print(A, C)
    move(n - 1, B, A, C)

print(2 * n + 1)
move(n, 1, 2, 3)
