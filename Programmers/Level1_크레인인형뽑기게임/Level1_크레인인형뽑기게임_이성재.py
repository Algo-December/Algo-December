def solution(board, moves):
    depth = len(board)

    def pick(number):
        for i in range(depth):
            k = board[i][number - 1]
            if k:
                board[i][number - 1] = 0
                return k
        return 0
    
    answer = 0
    right_stack = []

    for move in moves:
        num = pick(move)
        if num:
            if right_stack and right_stack[-1] == num:
                right_stack.pop()
                answer += 2
            else:
                right_stack.append(num)
        
    print(right_stack)


    return answer



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))