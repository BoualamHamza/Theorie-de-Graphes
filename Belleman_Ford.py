# the belleman Ford Algorithm allows you to find the shortest path from a node called the source to 'all' the other nodes , even if the weights are negative that's the difference betweenhim and Dijkstra

from OrientedGraph import Graph


class BellmanFord:
    def __init__(self, graph):
        self.graph = graph

    def shortestPath(self, source):
        # first step is to initialize
        distances = {node: float('inf') for node in self.graph.graph}
        distances[source] = 0
        # second step is to relax
        for _ in range(len(distances)):
            for u in self.graph.graph:
                for v, weight in self.graph.graph[u].items():
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        # third step is to check for negative cycles
        for u in self.graph.graph:
            for v, weight in self.graph.graph[u].items():
                if distances[u] + weight < distances[v]:
                    return False
        return distances
