import sys
input = sys.stdin.readline

def get_gap(star):  # comb_half로 고른 star팀과 안고른 link 팀의 점수 차이 계산
    link = [i for i in range(1, n) if i not in star]
    score_star = 0
    score_link = 0
    for i in star:
        for j in star:
            score_star += graph[i][j]

    for i in link:
        for j in link:
            score_link += graph[i][j]

    return abs(score_link - score_star)


def comb_half(level):  # n개 중 절반 고르는 함수
    global answer
    if len(result) == n // 2 - 1:  # (n//2- 1) 개만 고르고 0을 추가한다.
        gap = get_gap([0] + result)
        answer = min(answer, gap)
        if answer == 0:
            print(0)
            sys.exit()
        return

    if level == n:
        return

    result.append(level)
    comb_half(level + 1)
    result.pop()
    comb_half(level + 1)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = []
answer = 1e10
comb_half(1)
print(answer)