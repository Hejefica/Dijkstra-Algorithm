from ImgResize import image_resize
from EdgeColor import EdgeColor
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import cv2

IATADictionary = {
    "MEX": "Benito Juarez Intl. Airport",
    "CUN": "Cancun Intl. Airport",
    "GDL": "Miguel Hidalgo y Costilla Intl. Airport",
    "MTY": "Gral. Mariano Escobedo Intl. Airport",    
    "TIJ": "Gral. Abelardo L. Rodriguez Intl. Airport",
    "SJD": "San Jose del Cabo Intl. Airport",
    "PVR": "Lic. Gustavo Diaz Ordaz Intl. Airport",
    "MID": "Manuel Crescencio Rejon Intl. Airport",    
    "BJX": "Del Bajio Intl. Airport",     
    "CUL": "Bachigualato Intl. Airport",    
    "HMO": "Gral. Ignacio Pesqueira Garcia Intl. Airport",
    "CUU": "Gral. Roberto Fierro Villalobos Intl. Airport",
    "CJS": "Abraham Gonzalez Intl. Airport",
    "TGZ": "Angel Albino Corzo Intl. Airport",    
    "VER": "Gral. Heriberto Jara Intl. Airport", 
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
    return path

def print_graph(Airports, Path, init_graph):
    Graph = nx.Graph()
    Graph.add_nodes_from(Airports)
                                #    0      1      2      3      4      5      6       7     8      9     10     11     12     13     14     15     16     17     18     19     20     21     22     23     24     25     26     27     28     29     30    
    Edges = pd.DataFrame({'from': ['TIJ', 'TIJ', 'TIJ', 'HMO', 'HMO', 'HMO', 'HMO', 'CJS', 'CJS', 'CUU', 'CUU', 'CUU', 'CUL', 'CUL', 'CUL', 'CUL', 'MTY', 'PVR', 'PVR', 'GDL', 'GDL', 'MEX', 'MEX', 'MEX', 'VER', 'VER', 'VER', 'TGZ', 'TGZ', 'MID', 'MID'], 
                            'to': ['CJS', 'HMO', 'SJD', 'CJS', 'CUU', 'CUL', 'SJD', 'MTY', 'CUU', 'MTY', 'BJX', 'CUL', 'SJD', 'PVR', 'GDL', 'BJX', 'BJX', 'SJD', 'GDL', 'BJX', 'MEX', 'BJX', 'VER', 'MTY', 'MTY', 'MID', 'TGZ', 'MID', 'CUN', 'MTY', 'CUN']})

    EdgeColors = ["blue" for x in range(31)]
    EdgeWidths = [1 for x in range(31)]

    for p in range(len(Path)-1):
        PathTempArray = [Path[p], Path[p+1]]
        EdgeColor(PathTempArray, EdgeColors, EdgeWidths)           

    Graph = nx.from_pandas_edgelist(Edges, 'from', 'to', create_using = nx.Graph())

    Positions = {"MEX": (125, 25), "CUN": (210, 35), "GDL": (100, 30), "MTY": (120, 75), "TIJ": (5, 125),
                "SJD": (55, 55), "PVR": (85, 33), "MID": (190, 35), "BJX": (110, 40), "CUL": (70, 70),
                "HMO": (45, 95), "CUU": (80, 90), "CJS": (75, 120), "TGZ": (170, 5), "VER": (145, 20)}

    nx.draw(Graph, pos = Positions, node_color = 'black', with_labels = True, font_size = 7, 
            font_color = "white", width = EdgeWidths, edge_color = EdgeColors)

    nx.draw_networkx_edge_labels(Graph, pos = Positions, edge_labels = {
        ("TIJ", "CJS") : init_graph["TIJ"]["CJS"],
        ("TIJ", "HMO") : init_graph["TIJ"]["HMO"], 
        ("TIJ", "SJD") : init_graph["TIJ"]["SJD"],
        ("HMO", "CJS") : init_graph["HMO"]["CJS"],
        ("HMO", "CUU") : init_graph["HMO"]["CUU"],
        ("HMO", "CUL") : init_graph["HMO"]["CUL"],
        ("HMO", "SJD") : init_graph["HMO"]["SJD"], 
        ("CJS", "MTY") : init_graph["CJS"]["MTY"],
        ("CJS", "CUU") : init_graph["CJS"]["CUU"],
        ("CUU", "MTY") : init_graph["CUU"]["MTY"],
        ("CUU", "BJX") : init_graph["CUU"]["BJX"],
        ("CUU", "CUL") : init_graph["CUU"]["CUL"], 
        ("CUL", "HMO") : init_graph["CUL"]["HMO"],
        ("CUL", "SJD") : init_graph["CUL"]["SJD"],
        ("CUL", "PVR") : init_graph["CUL"]["PVR"],
        ("CUL", "GDL") : init_graph["CUL"]["GDL"],
        ("CUL", "BJX") : init_graph["CUL"]["BJX"], 
        ("MTY", "BJX") : init_graph["MTY"]["BJX"],
        ("SJD", "PVR") : init_graph["SJD"]["PVR"],
        ("PVR", "GDL") : init_graph["PVR"]["GDL"],
        ("GDL", "BJX") : init_graph["GDL"]["BJX"],
        ("GDL", "MEX") : init_graph["GDL"]["MEX"], 
        ("BJX", "MEX") : init_graph["BJX"]["MEX"],
        ("MEX", "MTY") : init_graph["MEX"]["MTY"],
        ("MEX", "VER") : init_graph["MEX"]["VER"],
        ("VER", "MTY") : init_graph["VER"]["MTY"],
        ("VER", "MID") : init_graph["VER"]["MID"], 
        ("VER", "TGZ") : init_graph["VER"]["TGZ"],
        ("TGZ", "MID") : init_graph["TGZ"]["MID"],
        ("TGZ", "CUN") : init_graph["TGZ"]["CUN"],
        ("MID", "MTY") : init_graph["MID"]["MTY"],
        ("MID", "CUN") : init_graph["MID"]["CUN"]})

    cv2.imshow("Mexico Intl. Airports", image_resize(cv2.imread("Map.jpg"), Height = 600))
    cv2.moveWindow('Mexico Intl. Airports', 900, 75)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows() 