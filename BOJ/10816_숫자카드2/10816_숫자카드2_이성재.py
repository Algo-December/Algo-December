import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
quests = list(map(int, input().split()))

counters = {}
for number in numbers:
    counters[number] = counters.get(number, 0) + 1

for quest in quests:
    print(counters.get(quest, 0), end=' ')


"""
from collections import Counter
"""