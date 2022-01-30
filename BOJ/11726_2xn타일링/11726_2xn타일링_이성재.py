import sys
input = sys.stdin.readline

n = int(input())
a, b = 1, 2
for _ in range(n - 2):
    c = (a + b) % 10007
    a = b % 10007
    b = c % 10007

if n == 1:
    print(1)
else:
    print(b % 10007)