def backtrack(level, visited, result):
    if level == n + 1:
        answer.append(''.join(map(str, result)))
        return
    
    for i in range(10):
        if (1 << i) & visited:
            continue
        if level == 0:
            backtrack(1, 1 << i, [i])
            continue
        if s[level - 1] == '>' and result[-1] > i:
            backtrack(level + 1, visited | (1 << i), result + [i])
        elif s[level - 1] == '<' and result[-1] < i:
            backtrack(level + 1, visited | (1 << i), result + [i])


n = int(input())
s = input().split()
answer = []
backtrack(0, 0, [])

print(answer[-1])
print(answer[0])