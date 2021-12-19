import sys
input = sys.stdin.readline


def make_progression(idx):
    global complete

    if idx == n:
        complete = 1
        print(''.join(map(str, result)))
        return

    if idx == 0:  # 첫 숫자는 무조건 1
        result.append(1)
        make_progression(idx + 1)
        return

    for num in range(1, 4):  # 1, 2, 3
        if complete:
            return

        result.append(num)  # 일단 넣기

        flag = 0
        i, j = -2, -1  # i:앞패턴 인덱스, j:뒤패턴 인덱스
        while i >= -len(result):
            if result[i:j] == result[j:]:
                result.pop()
                flag = 1
                break
            i -= 2
            j -= 1

        if not flag:
            make_progression(idx + 1)
            result.pop()


n = int(input())

result = []
complete = 0
make_progression(0)