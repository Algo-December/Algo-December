def solution(survey, choices):
    answer = ""
    scores = {"R": 0, "C": 0, "J": 0, "A": 0}
    for question, score in zip(survey, choices):
        disagree, agree = question[0], question[1]
        if disagree in scores:
            scores[disagree] -= score - 4
        else:
            scores[agree] += score - 4

    for question in ["RT", "CF", "JM", "AN"]:
        if scores[question[0]] >= 0:
            answer += question[0]
        else:
            answer += question[1]

    return answer
