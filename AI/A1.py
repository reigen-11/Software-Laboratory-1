def dfs(adj_matrix, start_vertex, visited):
    visited[start_vertex] = True
    print(start_vertex)

    for neighbor in range(len(adj_matrix)):
        if adj_matrix[start_vertex][neighbor] == 1 and not visited[neighbor]:
            dfs(adj_matrix, neighbor, visited)


def bfs_recursive(graph, start, visited_node=None):
    if visited_node is None:
        visited_node = set()
    visited_node.add(start)
    print(start, end=" ")

    for neighbor, connected in enumerate(graph[start]):
        if connected and neighbor not in visited_node:
            bfs_recursive(graph, neighbor, visited_node)


# Example usage:
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

num_vertices = len(adjacency_matrix)
visited = [False] * num_vertices

for vertex in range(num_vertices):
    if not visited[vertex]:
        dfs(adjacency_matrix, vertex, visited)

print(bfs_recursive(adjacency_matrix, 3))
