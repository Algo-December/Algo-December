import sys
input = sys.stdin.readline

def combination(level, cnt):
    global result
    if level == k:
        if cnt == 6:  # 6개를 고른 경우만 print
            print(' '.join(map(str, result)))
        return

    result.append(S[level])
    combination(level + 1, cnt + 1)
    result.pop()
    combination(level + 1, cnt)

while (line:=input().rstrip()) != '0':  # := walus operator, 할당 연산자
    numbers = list(map(int, line.split()))
    k = numbers[0]
    S = numbers[1:]
    result = []
    combination(0, 0)
    print()