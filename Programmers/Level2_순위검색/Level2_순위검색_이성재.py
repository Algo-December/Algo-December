from bisect import bisect_left

lang = ['java', 'cpp', 'python', '-']
job = ['backend', 'frontend', '-']
career = ['junior', 'senior', '-']
food = ['pizza', 'chicken', '-']

def solution(info, query):
    answer = []
    info = [string.split(' ') for string in info]
    info.sort(key=lambda info: int(info[4]))
    
    all_person = {
        l: {j: {c: {f: [] for f in food} for c in career} for j in job} for l in lang
    }
    
    for i in info:
        l, j, c, f, score = i
        for x in [l, '-']:
            for y in [j, '-']:
                for z in [c, '-']:
                    for w in [f, '-']:
                        all_person[x][y][z][w].append(int(score))
    
    for q in query:
        temp = q.split(' and ')
        temp += temp.pop().split(' ')
        l, j, c, f, score = temp
        
        idx = bisect_left(all_person[l][j][c][f], int(score))
        answer.append(len(all_person[l][j][c][f]) - idx)

        
    return answer