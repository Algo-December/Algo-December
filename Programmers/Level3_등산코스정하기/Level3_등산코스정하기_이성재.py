from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    is_gate = [False] * (n + 1)
    is_summit = [False] * (n + 1)

    for gate in gates:
        is_gate[gate] = True
    for summit in summits:
        is_summit[summit] = True

    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    def get_min_intensity(start_summit):
        heap = [(0, start_summit)]
        intensities = [1e10] * (n + 1)
        intensities[start_summit] = 0
        while heap:
            cur_intensity, node = heappop(heap)
            if intensities[node] < cur_intensity:
                continue

            if is_gate[node]:
                return cur_intensity

            for nxt_node, nxt_cost in graph[node]:
                if is_summit[nxt_node]:
                    continue
                if max(cur_intensity, nxt_cost) >= intensities[nxt_node]:
                    continue
                intensities[nxt_node] = max(cur_intensity, nxt_cost)
                heappush(heap, (max(cur_intensity, nxt_cost), nxt_node))

        return 1e10

    min_intensity = 1e10
    min_summit = -1
    for summit in sorted(summits):
        result = get_min_intensity(summit)
        if result < min_intensity:
            min_intensity = result
            min_summit = summit

    return [min_summit, min_intensity]
