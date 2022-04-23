def solution(s):
    s = s[1:-1]
    stack = []
    for x in s:
        if x == '{':
            stack.append([])
            temp = ''
        elif x == '}':
            stack[-1] += temp.split(',')
        elif x != '}':
            temp += x
    
    counter = {}
    for numbers in stack:
        for number in numbers:
            counter[number] = counter.get(number, 0) + 1

    answer = [0] * len(counter)
    for key, count in counter.items():
        answer[-count] = int(key)

    return answer

print(solution("{{20,111},{111}}"))