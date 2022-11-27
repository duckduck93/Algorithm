from collections import deque


def is_valid(arg):
    stack = deque()
    for i, c in enumerate(arg):
        if c in ['(', '{', '[']:
            stack.append(c)
            continue

        if not stack:
            return False

        if c == ')':
            if stack[-1] != '(':
                return False
            stack.pop()
        elif c == '}':
            if stack[-1] != '{':
                return False
            stack.pop()
        elif c == ']':
            if stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0


def solution(s):
    answer = 0
    for _ in range(len(s)):
        s = s[1:] + s[:1]
        print('"{}"'.format(s), end=' ')
        if is_valid(s):
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution("[](){}", ))
    print(solution("}]()[{", ))
    print(solution("[)(]", ))
    print(solution("}}}", ))
