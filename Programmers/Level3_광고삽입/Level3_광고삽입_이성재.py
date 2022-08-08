def time2int(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def int2time(number):
    h, res = divmod(number, 3600)
    m, s = divmod(res, 60)
    return f"{h:02}:{m:02}:{s:02}"


def solution(play_time, adv_time, logs):
    n = time2int(play_time)
    adv = time2int(adv_time)
    time_line = [0] * (n + 1)

    # 시작점, 끝점 표시
    for log in logs:
        st, et = map(time2int, log.split("-"))
        time_line[st] += 1
        time_line[et] -= 1

    # 누적합으로 시작점부터 끝점 사이 채우기
    for i in range(1, n + 1):
        time_line[i] += time_line[i - 1]

    # 구간합을 구하기 위해 누적합
    presum = [0]
    for i in range(n + 1):
        presum.append(presum[i] + time_line[i])

    # 구간합이 최대인 부분 찾기
    max_value = 0
    max_left = 0
    for left in range(n + 1 - adv):
        right = left + adv
        if presum[right] - presum[left] > max_value:
            max_value = presum[right] - presum[left]
            max_left = left

    return int2time(max_left)
