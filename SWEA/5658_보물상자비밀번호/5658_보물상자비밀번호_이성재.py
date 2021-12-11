T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = input()
    numbers += numbers[:N // 4]  # 아래 반복문에서 인덱스 범위를 벗어나지 않게 하기
    passwords_set = set()

    for j in range(N // 4):  # j : 몇 번 돌렸나
        for i in range(4):   # i : 네 개 모서리 순회
            passwords_set.add(numbers[(N//4) * (i) + j: (N//4) * (i+1) + j])

    passwords_list = []
    for num in passwords_set:
        passwords_list.append(int(num, 16))  # 16진수 -> 10진수 변환 후 저장

    passwords_list.sort()
    print(f'#{tc} {passwords_list[-K]}')
