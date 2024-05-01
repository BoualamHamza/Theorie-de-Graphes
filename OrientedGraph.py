# https://www.kdnuggets.com/5-free-courses-to-master-data-science
#this class present a weighted oriented graph 
# the datastructure used here is dict 
# graph = {
#     'A': {'B': 5, 'C': 3},
#     'B': {'C': 2},
#     'C': {'D': 7}
# }
class OG:
    def __init__(self):
        self.graph = dict()

    def addEdge(self, u, v, weight):
        if u not in self.graph: 
            self.graph[u] =dict()
            self.graph[u][v] = weight

    def __str__(self):
        res = ""
        for node in self.graph:
            res += str(node) + " -> " + " -> ".join([f"{neighbor}:{weight}" for neighbor, weight in self.graph[node].items()]) + "\n"
        return res    
# usage:
g = Graph()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 2)
g.add_edge('C', 'D', 7)

print(g)