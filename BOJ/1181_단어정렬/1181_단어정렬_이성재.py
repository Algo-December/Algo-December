# 오늘날의 성재의 풀이
import sys
sys.stdin.readline

n = int(input())
words = set()
for _ in range(n):
    word = input().rstrip()
    words.add((len(word), word))

words = list(words)
words.sort()
for length, word in words:
    print(word)


# 과거의 성재의 풀이
import sys
input = sys.stdin.readline

n = int(input())
word_list = set()
for _ in range(n):
    word = input().strip()
    word_list.add(word)
    
word_list = list(word_list)
word_list.sort()
word_list.sort(key = len)

for word in word_list:
    print(word)

