class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.CreateGraph(nodes, init_graph)
        
    def CreateGraph(self, nodes, init_graph): # Makes sure that the graph is symmetrical (distance between A&B = B&A).
        graph = {}
        for Node in nodes:
            graph[Node] = {}
        graph.update(init_graph)
        
        for Node, Edges in graph.items():
            for AdjacentNode, value in Edges.items():
                if graph[AdjacentNode].get(Node, False) == False:
                    graph[AdjacentNode][Node] = value        
        return graph
    
    def Nodes(self):
        return self.nodes
    
    def NodeNeighbors(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def ValueBetween(self, node1, node2):
        return self.graph[node1][node2]