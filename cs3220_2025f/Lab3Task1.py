from pyvis.network import Network
from src.Lab3Task1Classes import *
from src.Lab3Task1Environment import *
from src.graphClass import Graph
from data.task1mapData import *

task1Graph = Task1Graph(task1WorldDicts, Task1Locations()) 

net_Task1 = Network(
    heading="Lab3. Task 1",
    bgcolor ="#242020",
    font_color = "white",
    height = "750px",
    width = "100%",
    directed = True
)
nodeColors={
    "start":"red",
    "goal": "green",
    "frontier": "orange",
    "expanded":"pink"
}

for node in task1Graph.nodes():
    x,y=task1Graph.getLocation(node)
    net_Task1.add_node(node, x=x, y=y)

edge_weights = {(k, v2) : k2 for k, v in task1WorldDicts.items() for k2, v2 in v.items()}

edges=[]
for node_source in task1Graph.nodes():
    for node_target, actCost in task1Graph.get(node_source).items():
        #action=vacuumWorld[node_source]
        #print(action)
        if (node_source,node_target) not in edges and (node_target, node_source):
            #net_VacuumWorld.add_edge(node_source,node_target, label=str(action))
            net_Task1.add_edge(node_source,node_target, label=edge_weights[(node_source,node_target)])
            edges.append((node_source,node_target))

net_Task1.show("Task1 Graph.html", notebook=False)