from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from DijkstraAlgorithm import DijkstraAlgorithm

Airports = ["MEX", "CUN", "GDL", "MTY", "TIJ", "SJD", "PVR", "MID", "BJX", "CUL", "HMO", "CUU", "CJS", "TGZ", "VER"] 
 
init_graph = {}
for node in Airports:
    init_graph[node] = {}
    
init_graph["TIJ"]["CJS"] = 620
init_graph["TIJ"]["HMO"] = 425
init_graph["TIJ"]["SJD"] = 785
init_graph["HMO"]["CJS"] = 327
init_graph["HMO"]["CUU"] = 309
init_graph["HMO"]["CUL"] = 372
init_graph["HMO"]["SJD"] = 419
init_graph["CJS"]["MTY"] = 558
init_graph["CJS"]["CUU"] = 205
init_graph["CUU"]["MTY"] = 413
init_graph["CUU"]["BJX"] = 603
init_graph["CUU"]["CUL"] = 288
init_graph["CUL"]["HMO"] = 372
init_graph["CUL"]["SJD"] = 181
init_graph["CUL"]["PVR"] = 316
init_graph["CUL"]["GDL"] = 396
init_graph["CUL"]["BJX"] = 462
init_graph["SJD"]["PVR"] = 334
init_graph["PVR"]["GDL"] = 127
init_graph["GDL"]["BJX"] = 123
init_graph["GDL"]["MEX"] = 286
init_graph["BJX"]["MEX"] = 190
init_graph["MEX"]["MTY"] = 444
init_graph["MEX"]["VER"] = 190
init_graph["VER"]["MTY"] = 523
init_graph["VER"]["MID"] = 442
init_graph["VER"]["TGZ"] = 275
init_graph["TGZ"]["MID"] = 374
init_graph["TGZ"]["CUN"] = 507
init_graph["MID"]["MTY"] = 742
init_graph["MID"]["CUN"] = 180


Graph = Graph(Airports, init_graph)
PreviousNodes, ShortestPath = DijkstraAlgorithm(Graph = Graph, StartNode = "TIJ")

def print_result(PreviousNodes, ShortestPath, StartNode, TargetNode):
    path = []
    node = TargetNode
    
    while node != StartNode:
        path.append(node)
        node = PreviousNodes[node]
    path.append(StartNode)
    
    print("The shortest path between: \n\n    Tijuana Gral. Abelardo L. Rodriguez Intl. (TIJ)\n    -\n    Cancun Intl. (CUN)\n")
    print("Route: "," > ".join(reversed(path)), " [{} miles].".format(ShortestPath[TargetNode]))

print_result(PreviousNodes, ShortestPath, "TIJ", "CUN")

Graph = nx.Graph()
Graph.add_nodes_from(Airports)

Edge = [("TIJ", "CJS"), ("TIJ", "HMO"), ("TIJ", "SJD"),("HMO", "CJS"), ("HMO", "CUU"),("HMO", "CUL"),
        ("HMO", "SJD"), ("CJS", "MTY"), ("CJS", "CUU"),("CUU", "MTY"), ("CUU", "BJX"),("CUU", "CUL"),
        ("CUL", "HMO"), ("CUL", "SJD"), ("CUL", "PVR"),("CUL", "GDL"), ("CUL", "BJX"),("SJD", "PVR"),
        ("PVR", "GDL"), ("GDL", "BJX"), ("GDL", "MEX"),("BJX", "MEX"), ("MEX", "MTY"),("MEX", "VER"),
        ("VER", "MTY"), ("VER", "MID"), ("VER", "TGZ"),("TGZ", "MID"), ("TGZ", "CUN"),("MID", "MTY"), ("MID", "CUN")]

Graph.add_edges_from(Edge)

Position = {"MEX": (125, 25), "CUN": (210, 40), "GDL": (100, 30), "MTY": (120, 75), "TIJ": (5, 125),
            "SJD": (55, 55), "PVR": (85, 33), "MID": (190, 35), "BJX": (110, 40), "CUL": (70, 70),
            "HMO": (45, 95), "CUU": (80, 90), "CJS": (75, 120), "TGZ": (170, 5), "VER": (145, 20)}

class Tuple:
    def _init_(self, x, y):
        self.x = x
        self.y = y

P1 = Tuple()
P1.x = Position["MEX"][0]
P1.y = Position["MEX"][1]
P2 = Tuple()
P2.x = Position["CUN"][0]
P2.y = Position["CUN"][1]
P3 = Tuple()
P3.x = Position["GDL"][0]
P3.y = Position["GDL"][1]
P4 = Tuple()
P4.x = Position["MTY"][0]
P4.y = Position["MTY"][1]
P5 = Tuple()
P5.x = Position["TIJ"][0]
P5.y = Position["TIJ"][1]
P6 = Tuple()
P6.x = Position["SJD"][0]
P6.y = Position["SJD"][1]
P7 = Tuple()
P7.x = Position["PVR"][0]
P7.y = Position["PVR"][1]
P8 = Tuple()
P8.x = Position["MID"][0]
P8.y = Position["MID"][1]
P9 = Tuple()
P9.x = Position["BJX"][0]
P9.y = Position["BJX"][1]
P10 = Tuple()
P10.x = Position["CUL"][0]
P10.y = Position["CUL"][1]
P11 = Tuple()
P11.x = Position["HMO"][0]
P11.y = Position["HMO"][1]
P12 = Tuple()
P12.x = Position["CUU"][0]
P12.y = Position["CUU"][1]
P13 = Tuple()
P13.x = Position["CJS"][0]
P13.y = Position["CJS"][1]
P14 = Tuple()
P14.x = Position["TGZ"][0]
P14.y = Position["TGZ"][1]
P15 = Tuple()
P15.x = Position["VER"][0]
P15.y = Position["VER"][1]

Nodes = {"MEX": P1, "CUN": P2, "GDL": P3, "MTY": P4, "TIJ": P5, "SJD": P6, "PVR": P7, "MID": P8, 
        "BJX": P9, "CUL": P10, "HMO": P11, "CUU": P12, "CJS": P13, "TGZ": P14, "VER": P15}

EdgeColors = ['blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'blue', 'red', 'blue',
              'red', 'blue', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
              'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue']

EdgeWidths = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]
          
nx.draw(Graph, pos = Position, node_color = 'black', with_labels = True, font_size = 7, 
        font_color = "white", width = EdgeWidths, edge_color = EdgeColors)
plt.show()