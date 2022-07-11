def solution(user_id, banned_id):
    def compare(id, pattern):
        if len(id) != len(pattern):
            return False
        for i in range(len(id)):
            if pattern[i] != '*' and id[i] != pattern[i]:
                return False
        return True

    def dfs(level, comb):
        # base case
        if level == len(banned_id)-1:
            tmp = list(set(comb))
            if len(tmp) == len(comb):
                cases.add(tuple(sorted(tmp)))
            return
        for nj in range(len(combs[level+1])):
            if combs[level+1][nj] not in comb:
                dfs(level+1, comb+[combs[level+1][nj]])

    combs = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if compare(user, ban):
                tmp.append(user)
        combs.append(tmp)

    cases = set()
    for j in range(len(combs[0])):
        dfs(0, [combs[0][j]])

    return len(cases)


result = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(result)