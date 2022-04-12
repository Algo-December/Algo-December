def solution(id_list, reports, k):
    n = len(id_list)
    answer = [0] * n

    index_dict = {id_list[i]: i for i in range(n)}
    report_dict = {}  # key: 신고당한 사람, value: 신고한 사람 set
    
    for report in reports:
        reporter, loser = report.split()
        if loser in report_dict:
            report_dict[loser].add(reporter)
        else:
            report_dict[loser] = {reporter}
            
        
    for _, value in report_dict.items():
        if len(value) >= k:
            for reporter in value:
                answer[index_dict[reporter]] += 1
        
    return answer