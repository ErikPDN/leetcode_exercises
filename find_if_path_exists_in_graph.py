from collections import deque


def valid_path(n, edges, source, destination):
    graph = []
    for i in range(n):
        graph.append([])

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    visited.add(source)
    queue = deque([source])

    while queue:
        current = queue.popleft()
        if current == destination:
            return True

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(valid_path(n, edges, source, destination))
