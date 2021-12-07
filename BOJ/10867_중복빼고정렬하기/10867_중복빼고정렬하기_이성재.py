import sys
input = sys.stdin.readline

n = int(input())
numbers_set = set(map(int, (input().split())))

numbers = list(numbers_set)
numbers.sort()
for number in numbers:
    print(number, end=' ')