import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

IATADictionary = {
    "MEX": "Benito Juárez Intl. Airport",
    "CUN": "Cancun Intl. Airport",
    "GDL": "Miguel Hidalgo y Costilla Intl. Airport",
    "MTY": "General Mariano Escobedo Intl. Airport",    
    "TIJ": "General Abelardo L. Rodriguez Intl. Airport",
    "SJD": "San José del Cabo Intl. Airport",
    "PVR": "Licenciado Gustavo Díaz Ordaz Intl. Airport",
    "MID": "Manuel Crescencio Rejón Intl. Airport",    
    "BJX": "Del Bajio Intl. Airport",     
    "CUL": "Bachigualato Intl. Airport",    
    "HMO": "General Ignacio Pesqueira García Intl. Airport",
    "CUU": "General Roberto Fierro Villalobos Intl. Airport",
    "CJS": "Abraham Gonzalez Intl. Airport",
    "TGZ": "Ángel Albino Corzo Intl. Airport",    
    "VER": "General Heriberto Jara Intl. Airport", 
}

def print_result(PreviousNodes, ShortestPath, StartNode, TargetNode):
    path = []
    node = TargetNode
    
    while node != StartNode:
        path.append(node)
        node = PreviousNodes[node]
    path.append(StartNode)
    
    print("The shortest path between:\n\n\t", IATADictionary[StartNode], "(", StartNode, ").", 
    "\n\t-\n\t", IATADictionary[TargetNode], "(", TargetNode, ").\n")
    print("Route: "," > ".join(reversed(path)), " [{} miles].".format(ShortestPath[TargetNode]))
    print(path)

def print_graph(Airports):
    Graph = nx.Graph()
    Graph.add_nodes_from(Airports)

    Edges = pd.DataFrame({'from': ['TIJ', 'TIJ', 'TIJ', 'HMO', 'HMO', 'HMO', 'HMO', 'CJS', 'CJS', 'CUU', 'CUU', 'CUU', 'CUL', 'CUL', 'CUL', 'CUL', 'CUL', 'PVR', 'PVR', 'GDL', 'GDL', 'MEX', 'MEX', 'MEX', 'VER', 'VER', 'VER', 'TGZ', 'TGZ', 'MID', 'MID'], 
                            'to': ['CJS', 'HMO', 'SJD', 'CJS', 'CUU', 'CUL', 'SJD', 'MTY', 'CUU', 'MTY', 'BJX', 'CUL', 'HMO', 'SJD', 'PVR', 'GDL', 'BJX', 'SJD', 'GDL', 'BJX', 'MEX', 'BJX', 'VER', 'MTY', 'MTY', 'MID', 'TGZ', 'MID', 'CUN', 'MTY', 'CUN']})


    EdgeColors = ['blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'blue', 'red', 'green',
                'red', 'blue', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
                'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue']

    EdgeWidths = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]

    Graph = nx.from_pandas_edgelist(Edges, 'from', 'to', create_using = nx.Graph())

    Positions = {"MEX": (125, 25), "CUN": (210, 40), "GDL": (100, 30), "MTY": (120, 75), "TIJ": (5, 125),
                "SJD": (55, 55), "PVR": (85, 33), "MID": (190, 35), "BJX": (110, 40), "CUL": (70, 70),
                "HMO": (45, 95), "CUU": (80, 90), "CJS": (75, 120), "TGZ": (170, 5), "VER": (145, 20)}

    nx.draw(Graph, pos = Positions, node_color = 'black', with_labels = True, font_size = 7, 
            font_color = "white", width = EdgeWidths, edge_color = EdgeColors)

    nx.draw_networkx_edge_labels(Graph, pos = Positions, edge_labels = {("TIJ", "CJS") : 620, ("TIJ", "HMO") : 425, 
    ("TIJ", "SJD") : 785, ("HMO", "CJS") : 327, ("HMO", "CUU") : 309, ("HMO", "CUL") : 372, ("HMO", "SJD") : 419, 
    ("CJS", "MTY") : 558, ("CJS", "CUU") : 205, ("CUU", "MTY") : 413, ("CUU", "BJX") : 603, ("CUU", "CUL") : 288, 
    ("CUL", "HMO") : 372, ("CUL", "SJD") : 181, ("CUL", "PVR") : 316, ("CUL", "GDL") : 396, ("CUL", "BJX") : 462, 
    ("SJD", "PVR") : 334, ("PVR", "GDL") : 127, ("GDL", "BJX") : 123, ("GDL", "MEX") : 286, ("BJX", "MEX") : 190, 
    ("MEX", "MTY") : 444, ("MEX", "VER") : 190, ("VER", "MTY") : 523, ("VER", "MID") : 442, ("VER", "TGZ") : 275, 
    ("TGZ", "MID") : 374, ("TGZ", "CUN") : 507, ("MID", "MTY") : 742, ("MID", "CUN") : 180})

    plt.show()