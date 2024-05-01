import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from dijkstra import Dijkstra

class Visualization:
    def __init__(self):
        self.graph = Graph()

    def add_edge(self, u, v, weight):
        self.graph.add_edge(u, v, weight)

    def plot_graph(self):
        G = nx.DiGraph()
        for u in self.graph.graph:
            for v, weight in self.graph.graph[u].items():
                G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, font_weight="bold", arrows=True)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def visualize_algorithm(self, algorithm, start_node):
        if algorithm == 'Dijkstra':
            d = Dijkstra(self.graph)
            distances = d.shortest_path(start_node)
            print("Shortest distances from node {} using Dijkstra's algorithm:".format(start_node))
            print(distances)
        else:
            print("Invalid algorithm!")

# Example usage:
if __name__ == "__main__":
    v = Visualization()

    v.add_edge('A', 'B', 5)
    v.add_edge('A', 'C', 3)
    v.add_edge('B', 'C', 2)
    v.add_edge('C', 'D', 7)

    v.plot_graph()
    v.visualize_algorithm('Dijkstra', 'A')
