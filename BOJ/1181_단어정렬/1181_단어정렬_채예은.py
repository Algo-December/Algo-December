import sys
input = sys.stdin.readline

n = int(input())
words = []
max_len = 0
for _ in range(n):
    word = input().rstrip()
    words.append(word)
    if len(word) > max_len:
        max_len = len(word)

# words.sort(key=lambda x: len(x))

matrix = [[] for _ in range(max_len)]





print(words)

