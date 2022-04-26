
def solution(N, stages):
    solved = [0] * (N + 1)
    trying = [0] * (N + 2)

    for stage in stages:
        trying[stage] += 1
        for i in range(1, stage):
            solved[i] += 1
    
    results = []
    for i in range(1, N+1):
        if solved[i]+trying[i]:
            results.append(((trying[i]/(solved[i]+trying[i])), i+1))
        else:
            results.append((0, i+1))

    results.sort(key=lambda arr: (-arr[0], arr[1]))
    answer = [result[1]-1 for result in results]

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 5
# stages = [1, 1, 1, 1, 1, 1]
print(solution(N, stages))