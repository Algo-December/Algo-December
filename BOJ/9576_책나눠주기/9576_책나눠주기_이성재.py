import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # 가장 오른쪽 책을 기준으로 정렬
    students = sorted(
            [tuple(map(int, input().split())) for _ in range(m)],
            key=lambda arr: arr[1]
        )
    answer = 0
    used_book = [False] * (n + 1)

    for a, b in students:  
        for i in range(a, b + 1):  # 이 학생이 갖고 싶은 책들 중
            if not used_book[i]:   # 사용되지 않은 책 중 최대한 왼쪽에 있는 책 선택
                used_book[i] = True
                answer += 1
                break

    print(answer)