def solution(record):
    answer = []
    result = []
    nickname = {}

    for rec in record:
        temp = rec.split()
        if temp[0] == 'Enter':
            uid, nick = temp[1:]
            nickname[uid] = nick
            result.append((uid, True))

        elif temp[0] == 'Leave':
            uid = temp[1]
            result.append((uid, False))

        elif temp[0] == 'Change':
            uid, nick = temp[1:]
            nickname[uid] = nick

    for uid, is_enter in result:
        if is_enter:
            answer.append(f'{nickname[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{nickname[uid]}님이 나갔습니다.')

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))