def solution(survey, choices):
    def find_index(question):
        if question in ['RT', 'TR']:
            return 1
        if question in ['CF', 'FC']:
            return 2
        if question in ['JM', 'MJ']:
            return 3
        if question in ['AN', 'NA']:
            return 4

    def find_score(question, answer):
        return (answer - 4) * (1 if question[0] > question[1] else -1)

    def find_result(personality):
        result = ''
        result += 'R' if personality[1] >= 0 else 'T'
        result += 'C' if personality[2] >= 0 else 'F'
        result += 'J' if personality[3] >= 0 else 'M'
        result += 'A' if personality[4] >= 0 else 'N'
        return result

    p = {
        1: 0, 2: 0, 3: 0, 4: 0,
    }
    for i, q in enumerate(survey):
        index = find_index(q)
        p[index] += find_score(q, choices[i])

    return find_result(p)


if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))
