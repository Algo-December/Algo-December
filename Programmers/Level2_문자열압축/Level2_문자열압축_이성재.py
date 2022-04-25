def solution(s):
    answer = 1000000
    n = len(s)

    if n == 1:
        return 1

    for unit_len in range(1, n // 2 + 1):  # 단위 길이로 압축.
        result = ''     # 최종적으로 압축된 문자열
        curr_unit = ''  # 현재 단위 문자열
        curr_num = 0    # 현재 압축된 문자열 수

        for start in range(0, n, unit_len):
            unit = s[start: start+unit_len]  # 단위 길이 문자열

            if unit != curr_unit:
                if curr_num > 1:             # 압축이 가능한 경우만 압축 
                    result += str(curr_num)

                curr_num = 1
                result += unit
                curr_unit = unit
            else:
                curr_num += 1

        if curr_num > 1:
            result += str(curr_num)

        answer = min(answer, len(result))

    return answer