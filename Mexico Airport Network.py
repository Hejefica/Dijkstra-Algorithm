from Graph import Graph
from DijkstraAlgorithm import DijkstraAlgorithm
from Output import print_result
from Output import print_graph

Airports = ["MEX", "CUN", "GDL", "MTY", "TIJ", "SJD", "PVR", "MID", "BJX", "CUL", "HMO", "CUU", "CJS", "TGZ", "VER"] 
StartNode = "TIJ"
TargetNode = "MID"

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
init_graph["MTY"]["BJX"] = 342
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
PreviousNodes, ShortestPath = DijkstraAlgorithm(Graph = Graph, StartNode = StartNode)

Path = print_result(PreviousNodes, ShortestPath, StartNode, TargetNode)
print_graph(Airports, Path)