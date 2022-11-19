import sys
from collections import deque
from heapq import heappush, heappop


class Node:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.gate = False
        self.summit = False
        self.next = []

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        gate = 'O' if self.gate else 'X'
        summit = 'O' if self.summit else 'X'
        ne = ','.join(map(lambda x: '({},{})'.format(x[0], x[1]), self.next))
        return '{} (GATE {} | SUMMIT {}) next:{}'.format(self.name, gate, summit, ne)


def make_graph(n, paths, gates, summits):
    nodes = [Node(i) for i in range(n + 1)]
    for gate in gates:
        nodes[gate].gate = True
    for summit in summits:
        nodes[summit].summit = True

    for path in paths:
        node1, node2, duration = path

        nodes[node1].next.append([duration, node2])
        nodes[node2].next.append([duration, node1])

    nodes[0] = None
    return nodes


def find_path_bfs(n: int, nodes: [Node], start: int):
    visited = [-1] * (n + 1)

    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur = q.popleft()
        cur_node: Node = nodes[cur]

        nexts = cur_node.next
        for next_arr in nexts:
            distance, next = next_arr
            next_node = nodes[next]

            intensity = max(visited[cur], distance)
            if visited[next] == -1 and not next_node.gate and not next_node.summit:
                visited[next] = intensity
                q.append(next)
                continue
            if next_node.gate:
                continue
            if next_node.summit:
                visited[next] = min(visited[next], intensity) if visited[next] != -1 else intensity
                continue
            if visited[next] > intensity:
                visited[next] = intensity
                q.append(next)

    return visited


def find_path_heapq(n: int, graphs: [Node], gates: [int]):
    visited = [sys.maxsize] * (n + 1)
    q = []

    for gate in gates:
        heappush(q, (0, gate))
        visited[gate] = 0

    while q:
        intensity, cur = heappop(q)
        cur_node = graphs[cur]
        if cur_node.summit or intensity > visited[cur]:
            continue

        for distance, next in graphs[cur].next:
            new_intensity = max(intensity, distance)
            if new_intensity < visited[next]:
                visited[next] = new_intensity
                heappush(q, (new_intensity, next))

    return visited


def solution(n, paths, gates, summits):
    nodes = make_graph(n, paths, gates, summits)
    path = find_path_heapq(n, nodes, gates)

    answer = [0, sys.maxsize]
    for summit in sorted(summits):
        if path[summit] < answer[1]:
            answer = [summit, path[summit]]
    return answer

    print('----------------------------------------')
    nodes = make_graph(n, paths, gates, summits)
    for node in nodes:
        print(node)

    for start in gates:
        path = find_path_bfs(n, nodes, start)
        for end in summits:
            answer.append([start, end, path[end]])

    print('----------------------------------------')
    print(answer)
    answer = list(map(lambda x: x[1:], answer))
    print(answer)
    result = sorted(answer, key=lambda x: (x[1], x[0]), reverse=True)
    print(result)
    return result.pop()


if __name__ == '__main__':
    print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3],
                   [5]))
    print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
    print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
    print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
