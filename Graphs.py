import numpy as np
from pyvis.network import Network
import random
import string

def undirected_unweighted_graph(vertex_names: set):
    print("Undirected Unweighted Graph Generation from Given set of Vertices \n\t 0 : for no edge between vertices \n\t 1 : for presence of edge between vertices \n")
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
    
    matrix = graph_to_matrix(graph, vertex_names)

    return graph, matrix, arevertices

def graph_to_matrix(graph: dict, vertex_names: set):
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
    random_vertices = set()
    no_V = int(input("Number of Vertices : "))
    for i in range(no_V):
        random_alphabet = random.choice(string.ascii_uppercase)
        random_vertices.add(random_alphabet)
        graph = undirected_unweighted_graph(random_vertices)
        matrix = graph_to_matrix(graph, random_vertices)
    return graph, matrix, random_vertices

def visualize_graph(graph: dict, vertex_names: set):

    net = Network()
    for v1, e1 in graph.items():
        for v2, e2 in e1.items():
            net.add_node()


if __name__ == "__main__":
    vertex_names = {"A", "B", "C", "D"}
    undirected_graph, matrix_form, set_vertices = undirected_unweighted_graph(vertex_names)
    Random_graph, adjacency_matrix, random_vertices = generate_random_graph()

    
    print(f"{undirected_graph} \n {matrix_form} \n {set_vertices}")


