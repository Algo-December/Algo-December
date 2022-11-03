def solution(rows, cols, queries):
    def spin(x1, y1, x2, y2):
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        temp = matrix[x1][y1]
        min_value = temp

        for x in range(x1, x2):
            matrix[x][y1] = matrix[x + 1][y1]
            min_value = min(min_value, matrix[x + 1][y1])

        for y in range(y1, y2):
            matrix[x2][y] = matrix[x2][y + 1]
            min_value = min(min_value, matrix[x2][y + 1])

        for x in range(x2, x1, -1):
            matrix[x][y2] = matrix[x - 1][y2]
            min_value = min(min_value, matrix[x - 1][y2])

        for y in range(y2, y1, -1):
            matrix[x1][y] = matrix[x1][y - 1]
            min_value = min(min_value, matrix[x1][y - 1])

        matrix[x1][y1 + 1] = temp
        return min_value

    answer = []
    matrix = [[i + (cols * j) for i in range(1, cols + 1)] for j in range(rows)]
    for q in queries:
        answer.append(spin(*q))

    return answer
