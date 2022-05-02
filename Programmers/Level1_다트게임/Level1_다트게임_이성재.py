def solution(dartResult):
    stack = []
    for idx, char in enumerate(dartResult):
        if char.isdigit():
            if char == '0' and idx != 0 and dartResult[idx - 1] == '1':
                stack[-1] = 10
            else:
                stack.append(int(char))

        elif char == 'S':
            pass

        elif char == 'D':
            stack[-1] **= 2

        elif char == 'T':
            stack[-1] **= 3

        elif char == '*':
            stack[-1] *= 2
            if len(stack) > 1:
                stack[-2] *= 2

        elif char == '#':
            stack[-1] *= -1
            

    return sum(stack)



print(solution('1S2D*3T'))
print(solution('1D2S#10S'))