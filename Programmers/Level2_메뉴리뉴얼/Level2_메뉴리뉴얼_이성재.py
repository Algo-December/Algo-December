from itertools import combinations

def get_all_menu(order, num):
    combs = combinations(sorted(order), num)
    return [''.join(comb) for comb in combs]

def solution(orders, course):
    answer = []
    counter = {}

    for order in orders:
        for num in course:
            menus = get_all_menu(order, num)
            for menu in menus:
                counter[menu] = counter.get(menu, 0) + 1

    best_menu_dict = {num: (0, []) for num in course}
    for key, cnt in counter.items():
        if cnt < 2:
            continue
        n = len(key)
        max_cnt = best_menu_dict[n][0]
        if max_cnt > cnt:
            pass
        elif max_cnt < cnt:
            best_menu_dict[n] = (cnt, [key])
        elif max_cnt == cnt:
            best_menu_dict[n][1].append(key)

    for value in best_menu_dict.values():
        answer += value[1]

    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))



# 옛날 풀이
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        order_comb = []
        for order in orders:
            order_comb += combinations(sorted(order), num)
        most_ordered = Counter(order_comb).most_common()
        answer += [menus for menus, cnt in most_ordered if cnt > 1 and cnt == most_ordered[0][1]]
    return [''.join(a) for a in sorted(answer)]