import sys

def DijkstraAlgorithm(Graph, StartNode):
    UnvisitedNodes = list(Graph.Nodes())
    ShortestPath = {} # Updated cost of visiting each node.   
    PreviousNode = {} # Shortest known path to a node found so far.

    MaxValue = sys.maxsize    
    for Node in UnvisitedNodes:
        ShortestPath[Node] = MaxValue # Initialize the infinite value of unvisited nodes.   
    ShortestPath[StartNode] = 0 # Starting node's value with 0.
    
    while UnvisitedNodes: # Locates lowest value node.
        CurrentMinNode = None
        for Node in UnvisitedNodes:
            if CurrentMinNode == None:
                CurrentMinNode = Node
            elif ShortestPath[Node] < ShortestPath[CurrentMinNode]:
                CurrentMinNode = Node
                
        Neighbors = Graph.NodeNeighbors(CurrentMinNode) # Updates current node's neighbors distances.
        for Neighbor in Neighbors:
            TentativeValue = ShortestPath[CurrentMinNode] + Graph.ValueBetween(CurrentMinNode, Neighbor)
            if TentativeValue < ShortestPath[Neighbor]:
                ShortestPath[Neighbor] = TentativeValue
                PreviousNode[Neighbor] = CurrentMinNode # Updates the best path to current node.

        UnvisitedNodes.remove(CurrentMinNode) # Unflag visited node.
    
    return PreviousNode, ShortestPath