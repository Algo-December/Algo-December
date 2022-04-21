def solution(new_id):
    # level 1
    new_id = new_id.lower()

    # level 2
    special = '~!@#$%^&*()=+[{]}:?,<>/'
    for s in special:
        new_id = new_id.replace(s, '')

    # level 3
    word_list = new_id.split('.')
    a = []
    for word in word_list:
        if word == '':
            continue
        else:
            a.append(word)

    new_id = '.'.join(a)

    # level 4
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # level 5
    if not new_id:
        new_id = 'a'

    # level 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # level 7
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id