def solution(info, edges):
    def backtrack(sheep, wolf):
        nonlocal answer
        if sheep <= wolf:
            return
        answer = max(answer, sheep)

        for i in range(n):
            if not adjacency[i] or visited[i]:
                continue

            visited[i] = True
            adjacency[i] = False
            for nxt in graph[i]:
                adjacency[nxt] = True

            backtrack(sheep + int(info[i] == 0), wolf + int(info[i] == 1))

            visited[i] = False
            adjacency[i] = True
            for nxt in graph[i]:
                adjacency[nxt] = False

    n = len(info)
    graph = [[] for _ in range(n)]
    for p, c in edges:
        graph[p].append(c)

    visited = [False] * n
    adjacency = [False] * n  # 갈 수 있는 노드 표시

    visited[0] = True
    for nxt in graph[0]:
        adjacency[nxt] = True

    answer = 0
    backtrack(1, 0)

    return answer
