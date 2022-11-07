from collections import deque, defaultdict


def make_graph(n, roads):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    for road in roads:
        node1, node2 = road
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph


def find_path(graph, visited, source, destination):
    if len(graph[source]) == 0:
        return -1

    queue = deque()
    queue.append((source, 0))
    visited[source] = True

    while queue:
        current, count = queue.popleft()
        if current == destination:
            return count

        for next in graph[current]:
            if visited[next]:
                continue
            queue.append((next, count + 1))
            visited[next] = True
    return -1


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    result = [-1] * (n + 1)
    result[destination] = 0

    queue = deque()
    queue.append(destination)
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if result[next] != -1:
                continue
            result[next] = result[current] + 1
            queue.append(next)

    return list(result[s] for s in sources)


if __name__ == '__main__':
    print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
    print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
