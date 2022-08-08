def solution(gems):
    n = len(gems)
    total_cnt = len(set(gems))  # 총 보석 수
    result = []
    left, right = 0, 0  # 확인할 구간
    counter = {gems[0]: 1}  # 현재 구간에 대한 보석 개수 정보
    while left <= right < n:
        # 현재 구간에 모든 보석이 들어잇으면 구간 줄이기, 왼쪽 하나 빼기
        if len(counter) == total_cnt:
            result.append([left + 1, right + 1])  # 후보로 추가
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                counter.pop(gems[left])
            left += 1

        # 현재 구간에 보석이 모자라면 구간 늘리기, 오른쪽 하나 더 추가
        else:
            right += 1
            if right < n:
                counter[gems[right]] = counter.get(gems[right], 0) + 1

    result.sort(key=lambda arr: (arr[1] - arr[0], arr[0]))
    return result[0]
