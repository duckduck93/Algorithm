def solution(s):
    arr = s[1:-1].split('},{')
    for idx, arg in enumerate(arr):
        arr[idx] = set(map(lambda x: int(x), arg.replace('{', '').replace('}', '').split(',')))
    arr = sorted(arr, key=len)

    answer = []
    dup = set()
    length = 0
    for s in arr:
        for arg in s:
            dup.add(arg)
            if length != len(dup):
                answer.append(arg)
                length = len(dup)

    return answer


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution("{{20,111},{111}}"))
    print(solution("{{123}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
