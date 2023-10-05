import numpy as np

def undirected_unweighted_graph(vertex_names: set):
    graph = {vertex: {neighbor: 0 for neighbor in vertex_names if neighbor != vertex} for vertex in vertex_names}
    arevertices = set()

    for morty, rick in graph.items():
        for v2, n2 in rick.items():
            if (morty, v2) in arevertices or (v2, morty) in arevertices:
                graph[morty][v2] = graph[v2][morty]
            else:
                graph[morty][v2] = int(input(f"{morty} --> {v2} : "))
                graph[v2][morty] = graph[morty][v2]
                arevertices.add((morty, v2))
                arevertices.add((v2, morty))

    return graph

def graph_to_matrix(graph: dict, vertex_names: list):
    matrix = np.zeros((len(vertex_names), len(vertex_names)))

    for i, key1 in enumerate(vertex_names):
        for j, key2 in enumerate(vertex_names):
            if key1 == key2:
                matrix[i, j] = 0
            else:
                value2 = graph.get(key1, {}).get(key2, 0)
                matrix[i, j] = value2

    return matrix

def generate_random_graph():
    vertices = set()
    no_V = int(input("Number of Vertices : "))
    for i in range(no_V):
        random_alphabet = random.choice(string.ascii_uppercase)
        vertices.add(random_alphabet)
        graph = undirected_unweighted_graph(vertices)
    return graph, vertices


# if __name__ == "__main__":
#     vertex_names = ["A", "B", "C", "D"]
#     graph = undirected_unweighted_graph(vertex_names)
#     adjacency_matrix = graph_to_matrix(graph, vertex_names)
#
#     print("Graph:")
#     print(graph)
#     print("\nAdjacency Matrix:")
#     print(adjacency_matrix)


