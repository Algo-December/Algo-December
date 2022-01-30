n = int(input())
numbers = [*map(int, input().split())]

max_value = numbers[0]
dp = numbers[0]
for num in numbers[1:]:
    dp = max(dp + num, num)
    max_value = max(max_value, dp)

print(max_value)