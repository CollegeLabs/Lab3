from pyvis.network import Network
from src.Lab3Task1Environment import *
from data.task1mapData import *
from src.agents import ProblemSolvingNavAgentBFS
import streamlit as st
import streamlit.components.v1 as components
import networkx as nx

#task1Graph = Task1Graph(task1WorldDicts, Task1Locations()) 
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

def drawBtn(e,a,c):
    option= [e,a,c]
    st.button("Run One Agent's Step", on_click= AgentStep, args= [option])
    
def AgentStep(opt):
    st.header("Resolving Task 1 Problem ...")
    e,a,c= opt[0],opt[1],opt[2]
    if not st.session_state["clicked"]:
        st.session_state["env"]=e
        st.session_state["agent"]=a
        st.session_state["nodeColors"]=c    
    
    if e.is_agent_alive(a):
        e.step()
        st.success(" Agent now at : {}.".format(a.state))
        st.info("Current Agent performance {}:".format(a.performance))
        c[a.state]="orange"
        st.info("State of the Environment:")
        buildGraph(e.status, c) 
    else:
        if a.state==a.goal:
            st.success(" Agent now at the goal state: {}.".format(a.state))
        else:
            st.error("Agent in location {} and it is dead.".format(a.state))
        
    st.session_state["clicked"] = True
        
        
def buildGraph(graphData, nodeColorsDict):
    net_Task1 = Network(
    bgcolor ="#242020",
    font_color = "white",
    height = "750px",
    width = "100%",
    directed = True
)
    nodes=graphData.nodes()
    # initialize graph
    g = nx.Graph()
    
    # add the nodes
    for node in nodes:
        g.add_node(node, color=nodeColorsDict[node])
    # g.add_nodes_from(nodes)
    # for node in g:
    #     #node["color"]=nodeColorsDict[node]
    #     node['color']="white"
    # add the edges
    edges=[]
    for node_source in graphData.nodes():
        for node_target, dist in graphData.get(node_source).items():
            if set((node_source,node_target)) not in edges:
                edges.append(set((node_source,node_target)))                
    g.add_edges_from(edges)
    
    # generate the graph
    net_Task1.from_nx(g)
    
    net_Task1.save_graph('Task1 Graph.html')
    HtmlFile = open(f'Task1 Graph.html', 'r', encoding='utf-8')
    components.html(HtmlFile.read(), height = 1200,width=1000)
    
    
def makeDefaultColors(dictData):
    nodeColors=dict.fromkeys(dictData.keys(), "white")
    return nodeColors
        
    
def main():
    
        
    if "clicked" not in st.session_state:
        st.session_state["clicked"] = False
        
    if "env" not in st.session_state:
        st.session_state["env"]=None
        
    if "agent" not in st.session_state:
        st.session_state["agent"]=None
        
    if "nodeColors" not in st.session_state:
        st.session_state["nodeColors"]=None
        
    if not st.session_state["clicked"]:
        # Set header title
        st.header("Problem Solving Agents: Task1 Problem")
        st.header("_Initial Env._", divider=True)
        
        #TreasureGraph = TreasureMapGraph(GraphData)
        task1Graph = Task1Graph(task1WorldDicts, Task1Locations())
        nodeColors=makeDefaultColors(task1Graph.graph_dict)
        
        initState="LLLL"
        goalState="RRRR"
        
        #re=TreasureMapEnv(TreasureGraph)
        re=Task1Env(task1Graph)
        #BFSnavAgent=ProblemSolvingNavAgentBFS(initState,TreasureGraph,goalState)
        Task1SolveAgent=ProblemSolvingNavAgentBFS(initState, task1Graph, goalState)        
                      
        re.add_thing(Task1SolveAgent)
        st.header("State of the Environment", divider="red")
        nodeColors[Task1SolveAgent.state]="red"
        nodeColors[Task1SolveAgent.goal]="green"
        buildGraph(task1Graph, nodeColors) 
        st.info(f"The Agent in: {Task1SolveAgent.state} with performance {Task1SolveAgent.performance}.")
        st.info(f"The Agent goal is: {Task1SolveAgent.goal} .")
                
        drawBtn(re,Task1SolveAgent,nodeColors)
    
    if st.session_state["clicked"]:
        if st.session_state["env"].is_agent_alive(st.session_state["agent"]):
            #st.warning("Agent Step Done!")
            st.success(" Agent is working...")
            drawBtn(st.session_state["env"],st.session_state["agent"], st.session_state["nodeColors"])
       
    
#if __name__ == '__main__':
#    main()
    
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
#Task1SolveAgent("LLLL")
#Task1SolveAgent("RRRR")
with open("Task1 Graph.html", 'r', encoding='utf-8') as f:
    html_string=f.read()
components.html(html_string, height=750, width=1000)
#Task1SolveAgent2=ProblemSolvingNavAgentBFS(initState, task1Graph, goalState)

'''