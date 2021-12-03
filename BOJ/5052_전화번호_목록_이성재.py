import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    result = False
    n = int(input())
    phone_numbers = []
    for _ in range(n):
        phone = input().rstrip()
        phone_numbers.append(phone)

    phone_numbers.sort()
    for i in range(n - 1):
        l = len(phone_numbers[i])
        if phone_numbers[i + 1][:l] == phone_numbers[i]:
            result = True
            break

    if result:
        print('NO')
    else:
        print('YES')
    