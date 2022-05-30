def solution(info, query):
    COMMON_CODE = {'-': 0, 'cpp': 1, 'java': 2, 'python': 3, 'backend': 1, 'frontend': 2, 'junior': 1, 'senior': 2, 'chicken': 1, 'pizza': 2}

    applicants = []
    for person in info:
        tmp = person.split()
        applicant = []
        for t in tmp[:-1]:
            applicant.append(COMMON_CODE[t])
        applicant.append(int(tmp[-1]))
        applicants.append(applicant)

    answer = []
    for q in query:
        tmp = q.split()
        conditions = []
        for t in tmp[:-1]:
            if t != 'and':
                conditions.append(COMMON_CODE[t])
        conditions.append(int(tmp[-1]))

        # while 'and' in conditions:
        #     conditions.remove('and')

        def is_fit(arr):
            i = 0
            while i < 4:
                if conditions[i] != 0:
                    if arr[i] != conditions[i]:
                        return False
                i += 1
            return True

        over_x = list(filter(lambda x: x[-1] >= conditions[-1], applicants))  # 점수로 1차 필터링
        rst = list(filter(is_fit, over_x))  # 나머지 조건 필터링
        answer.append(len(rst))
    return answer


result = solution(
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    )
print(result)