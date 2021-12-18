import sys
n = int(input())

def backtrack(level, seq, history):
    # seq : 지금까지 만든 문자열
    # history : dictionary, history[i]: seq에 i가 들어있는 인덱스들 배열

    if level == n:
        print(seq)
        sys.exit()

    for i in ['1', '2', '3']:

        # 만약 i를 추가한 적 있으면
        if history[i]:
            if history[i][-1] == level - 1:  # 바로 이전에 i를 추가했다면 스킵
                continue

            # i를 추가해도 좋은 수열일지 확인
            flag = True
            for h in history[i]:
                gap = level - h   # gap: h ~ level까지 문자열의 길이
                if seq[h + 1 - gap: h] == seq[h + 1:]:  # h를 기준으로 '왼쪽 gap 길이의 문자열' 과 '오른쪽 gap 길이의 문자열' 비교
                    flag = False
                    break

            # 좋은 수열이면
            if flag:
                history[i].append(level)               # i를 level 인덱스에 추가했다고 기록
                backtrack(level + 1, seq + i, history)
                history[i].pop()                       # 기록해둔 i 다시 제거

        # 만약 i를 추가한 적 없으면
        else:
            history[i].append(level)               # i를 level 인덱스에 추가했다고 기록
            backtrack(level + 1, seq + i, history)
            history[i].pop()                       # 기록해둔 i 다시 제거

backtrack(0, '', {'1':[], '2':[], '3':[]})
