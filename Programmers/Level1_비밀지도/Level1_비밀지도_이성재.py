def convert(n, num):
    result = ''
    for i in range(n-1, -1, -1):
        if (1 << i) & num:
            result += '#'
        else:
            result += ' '
    return result 


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(convert(n, arr1[i] | arr2[i]))
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))