from heapq import heappop, heapify


def time2int(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def int2time(num):
    h, m = divmod(num, 60)
    return f"{h:02}:{m:02}"


def solution(n, t, m, timetable):
    heap = list(map(time2int, timetable))
    heapify(heap)

    now_time = time2int("09:00")
    for _ in range(n):
        bus = []
        while heap:
            # 만차거나 버스 시간보다 늦게 온 사람이면 그만 태워
            if len(bus) == m or heap[0] > now_time:
                break
            bus.append(heappop(heap))
        now_time += t

    # 마지막 버스가 만차면 마지막 탑승 시각보다 1분 빨리 오자
    if len(bus) == m:
        return int2time(bus[-1] - 1)
    # 마지막 버스에 자리가 있으면 마지막 버스 시각에 오자
    else:
        return int2time(now_time - t)
