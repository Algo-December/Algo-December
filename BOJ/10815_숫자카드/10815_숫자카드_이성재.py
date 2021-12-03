import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
quest = list(map(int, input().split()))

for q in quest:
    print(int(q in cards), end=' ')

# print(' '.join(map(str, [int(q in cards) for q in quest])))
# print(' '.join(list(map(lambda x: str(int(x in cards)), quest))))