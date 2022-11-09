from collections import deque, defaultdict


def bfs(n, graph):
    counter = [-1] * (n + 1)

    q = deque()
    q.append(1)
    counter[1] = 0

    while q:
        sta = q.popleft()
        next_nodes = graph[sta]

        for node in next_nodes:
            if counter[node] != -1:
                continue
            q.append(node)
            counter[node] = counter[sta] + 1

    return counter


def solution(n, edge):
    graph = defaultdict(list)
    for sta, end in edge:
        graph[sta].append(end)
        graph[end].append(sta)

    result = bfs(n, graph)
    max_distance = max(result)
    return len(list(filter(lambda arg: arg == max_distance, result)))


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
