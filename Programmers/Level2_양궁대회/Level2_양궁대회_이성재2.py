def cal_diff(ryan_info, apeach_info):
    result = 0
    for i in range(10):
        if ryan_info[i] == apeach_info[i] == 0:
            continue
        elif ryan_info[i] > apeach_info[i]:
            result += 10 - i
        else:
            result -= 10 - i
    return result


def solution(n, info):
    ryan_info = [0] * 11
    max_diff = 0
    answer = [-1]

    def backtrack(level, arrow_cnt):
        nonlocal max_diff, answer
        if level == -1:
            diff = cal_diff(ryan_info, info)
            if max_diff < diff:
                max_diff = diff
                answer = ryan_info[:]
            return

        if arrow_cnt < n:
            ryan_info[level] += 1
            backtrack(level, arrow_cnt + 1)
            ryan_info[level] -= 1

        backtrack(level - 1, arrow_cnt)

    backtrack(10, 0)

    return answer
