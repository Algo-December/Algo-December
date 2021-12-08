import itertools


def check_combs(combs):
    global answer, s1, s2
    for comb in combs:
        # 2명이 서로 같은 팀이 될 수 있는지 확인
        a = students[comb[0]]
        b = students[comb[1]]
        # 팀구성조건 4가지
        if a[0] == b[0]:
            return False
        elif 'I' in a[0] and 'I' in b[0]:
            return False
        elif ('T' in a[0] and 'P' not in b[0]) or ('T' in b[0] and 'P' not in a[0]):
            return False
        elif a[1] == 'O' and b[1] == 'O':
            return False

    # 체크 완료 => 가능한 조합!
    for comb in combs:
        a = students[comb[0]]
        b = students[comb[1]]
        power = int(a[2]) + int(b[2])
        if a[1] == 'O' or b[1] == 'O':
            power += 10
        if a[1] == b[1]:
            power -= 30
        if a[0][0] == 'E' and b[0][0] == 'E':
            power += 40
        if len(set(a[0] + b[0])) == 5:  # 3개가 같으면 set 결과가 5개가 된다.
            power += 40

        if power > answer:
            answer = power
            s1 = min(comb[0], comb[1]) + 1
            s2 = max(comb[0], comb[1]) + 1


def make_combs(n, rst):
    global cnt
    # 베이스케이스
    if len(rst) == n//2:
        # 조합 완성!
        check_combs(rst)
        return

    remains = [i for i in range(n) if not check[i]]
    tmps = list(itertools.combinations(remains, 2))
    for tmp in tmps:
        check[tmp[0]] = 1  # tmp = (0, 1)
        check[tmp[1]] = 1
        make_combs(n, rst + [tmp])
        check[tmp[0]] = 0
        check[tmp[1]] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    students = [input().split() for _ in range(n)]

    answer = -1
    s1 = s2 = 0
    check = [0] * n
    make_combs(n, [])

    if answer == -1:
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} {s1} {s2} {answer}')