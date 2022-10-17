def get_rank(value):
    return 7 - value if value > 1 else 6


def solution(lottos, win_nums):
    min_value = len(set(lottos) & set(win_nums))
    max_value = min_value + lottos.count(0)

    return [get_rank(max_value), get_rank(min_value)]
