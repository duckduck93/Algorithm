def make_tree(root, word):
    current = root
    for c in word:
        counter, node = current
        if c not in node:
            node[c] = [0, {}]
        current[0] += 1
        current = node[c]
    current[0] += 1
    return root


def find_count(root, word):
    count = 0
    current = root
    for c in word:
        counter, node = current
        if counter == 1:
            return count
        count += 1
        current = node[c]
    return count


def solution(words):
    answer = 0
    root = [0, {}]
    for word in words:
        make_tree(root, word)
    for word in words:
        answer += find_count(root, word)
    return answer


if __name__ == '__main__':
    print(solution(words=["go", "gone", "guild"]))
    print(solution(words=["abc", "def", "ghi", "jklm"]))
    print(solution(words=["word", "war", "warrior", "world"]))
