from pyvis.network import Network
from src.Lab3Task1Environment import *
from data.task1mapData import *
from src.agents import ProblemSolvingNavAgentBFS
import streamlit.components.v1 as components

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
'''
for node in task1Graph.nodes():
    x,y=task1Graph.getLocation(node)
    net_Task1.add_node(node, x=x, y=y)

edge_weights = {(k, v2) : k2 for k, v in task1WorldDicts.items() for k2, v2 in v.items()}

edges=[]
edge_weights=[]
for node_source in task1Graph.nodes():
    for node_target, actCost in task1Graph.get(node_source).items():
        if (node_source,node_target) not in edges and (node_target, node_source):
            net_Task1.add_edge(node_source,node_target, label=edge_weights[(node_source,node_target)])
            edges.append((node_source,node_target))
'''


net_Task1.add_nodes(task1Graph.nodes(), title=[str(node) for node in task1Graph.nodes()])

for node in net_Task1.nodes:
    if node['id']=='LLLL':
        node["color"]=nodeColors["start"]
    elif node['id']=='RRRR':
        node["color"]=nodeColors["goal"]

edges=[]
edges_labels=[]

#print(task1Graph.nodes())

for node_source in task1Graph.nodes():
    for action, node_target in task1WorldDicts.get(node_source).items():
        if set((node_source,action)) not in edges:
            net_Task1.add_edge(node_source, node_target, label=str(action)) 
            #dist is the actual node target while node target is the action to get to the next node
            edges.append(set((node_source,action)))
            edges_labels.append(str(node_target))

net_Task1.show("Task1 Graph.html", notebook=False)

initState='LLLL'
goalState='RRRR'
illegalStates = ["LRRR", "LRRB", "LBRR", "LRRL", "LLRR", "RLLR", "RRLL", "RLLB", "RBLL", "RLLL"]
#can't leave goat and cabbage or wolf and goat alone together (also covering all 3 without boat just in case)

Task1 = Task1ProblemGraph(initState, goalState, task1Graph)
Task1SolveAgent=ProblemSolvingNavAgentBFS(initState, task1Graph, goalState)

#print(Task1SolveAgent("LLLL"))
#Task1SolveAgent.run()
Task1SolveAgent("LLLL")
Task1SolveAgent("RRRR")
with open("Task1 Graph.html", 'r', encoding='utf-8') as f:
    html_string=f.read()
components.html(html_string, height=750, width=1000)
#Task1SolveAgent2=ProblemSolvingNavAgentBFS(initState, task1Graph, goalState)

