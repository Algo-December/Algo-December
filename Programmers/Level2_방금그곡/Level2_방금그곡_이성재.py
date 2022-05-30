def get_between_time(st, et):
    a, b = map(int, st.split(':'))
    c, d = map(int, et.split(':'))
    return (c - a) * 60 + d - b

def convert_sharp(melody):
    temp = []
    for m in melody:
        if m == '#':
            temp[-1] = temp[-1].lower()
        else:
            temp.append(m)
    return ''.join(temp)

def solution(m, musicinfos):
    m = convert_sharp(m)
    results = []
    for info in musicinfos:
        st, et, title, score = info.split(',')
        score = convert_sharp(score)
            
        time = get_between_time(st, et)
        k = len(score)
        q, r = divmod(time, k)
        
        music = score * q + score[:r]
        if m in music:
            results.append((len(music), title))
        
    results.sort(key=lambda arr: -arr[0])
    if results:
        return results[0][1]
            
    return '(None)'