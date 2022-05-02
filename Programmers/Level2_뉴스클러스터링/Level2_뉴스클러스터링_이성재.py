# 다중 집합 만들기
def get_multiset(word):
    result = []
    n = len(word)
    for i in range(n - 1):
        now = word[i:i+2]
        if now.isalpha():
            result.append(now)
    return result

# 배열에서 카운터 만들기
def counter(multiset):
    result = {}
    for x in multiset:
        result[x] = result.get(x, 0) + 1
    return result


def get_nu(set1, set2):
    counter1 = counter(set1)
    counter2 = counter(set2)

    ncounter = {}
    for x, cnt in counter1.items():
        if x in counter2:
            ncounter[x] = min(cnt, counter2[x])

    ucounter = counter1
    for x, cnt in counter2.items():
        ucounter[x] = max(ucounter.get(x, cnt), cnt)

    return sum(ncounter.values()), sum(ucounter.values())


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    set1 = get_multiset(str1)
    set2 = get_multiset(str2)

    a, b = get_nu(set1, set2)
    if b:
        return int(a * 65536 / b)
    else: 
        return 65536

print(solution('E=M*C^2', 'e=m*c^2'))