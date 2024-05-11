
class Prim:
    def __init__(self, graph):
        self.graph = graph

    def mst(self, source):
        priorities, pred, visited = dict(), dict(), set()
        for node in self.graph.graph:
            priorities[node] = float('inf')
            pred[node] = None
            visited.add(node)

        priorities[source] = 0
        while visited:
            current_node = min(visited, key=lambda node: priorities[node])
            visited.remove(current_node)

            for neighbor, weight in self.graph.graph[current_node].items():
                if neighbor in visited:
                    if weight < priorities[neighbor]:
                        priorities[neighbor] = weight
                        pred[neighbor] = current_node
        return pred
