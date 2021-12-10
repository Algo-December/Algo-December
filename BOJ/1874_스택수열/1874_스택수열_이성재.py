import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
numbers = list(range(n, 0, -1))
result = ''
try:
    for _ in range(n):
        k = int(input())
        while k > stack[-1]:  # 출력해야하는 숫자가 나올때까지 stack에 저장
            stack.append(numbers.pop())
            result += '+'
            
        stack.pop()  # 출력해야하는 숫자가 나왔으면 삭제
        result += '-'

    for char in result:
        print(char)

except:
    print('NO')

