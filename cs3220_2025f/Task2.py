from pyvis.network import Network 
import networkx as nx 
import streamlit as st
import streamlit.components.v1 as components #to display the HTML code
from src.TreasureMap import *
from src.graphClass import *
from src.TreasureMapEnv import TreasureMapEnv
from src.TreasureMapGraph import *
from src.TreasureMapproblem import *
from data.TreasureMapData import *
from src.agents import *
from src.Treasures import *


def drawBtn(e,a,c):
    option= [e,a,c]
    st.button("Run One Agent's Step", on_click= AgentStep, args= [option])
    
def AgentStep(opt):
    st.header("Resolving TreasureMap Navigation Problem ...")
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
    net = Network(
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%") 
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
    net.from_nx(g)
    
    net.save_graph('L3_TreasureMap.html')
    HtmlFile = open(f'L3_TreasureMap.html', 'r', encoding='utf-8')
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
        st.header("Problem Solving Agents: TreasureMap Navigation Problem")
        st.header("_Initial Env._", divider=True)
        
        TreasureGraph = TreasureMapGraph(GraphData)
        nodeColors=makeDefaultColors(TreasureGraph.graph_dict)
        
        initial_state = 'Room1'
        
        Env2=TreasureMapEnv(TreasureGraph)
        Pile_of_Gold = Gold()
        Diamond = D()
        flyer_for_100_free_pizzas = Pizza()
        twenty_extra_point_for_cs3220_final_exam = CSPoints()


        Env2.add_treasure(Pile_of_Gold)
        Env2.add_treasure(Diamond)
        Env2.add_treasure(flyer_for_100_free_pizzas)
        Env2.add_treasure(twenty_extra_point_for_cs3220_final_exam)

        T = random.choice([Pile_of_Gold, Diamond, flyer_for_100_free_pizzas, twenty_extra_point_for_cs3220_final_exam])
        Twogoals = [T, 'room48']
        BFSAP2 = ProblemSolvingNavAgentBFS(initial_state,TreasureGraph,Twogoals)       
                      
        Env2.add_thing(BFSAP2)
        st.header("State of the Environment", divider="red")
        nodeColors[BFSAP2.state]="red"
        nodeColors[BFSAP2.goal]="green"
        buildGraph(TreasureGraph, nodeColors) 
        st.info(f"The Agent in: {BFSAP2.state} with performance {BFSAP2.performance}.")
        st.info(f"The Agent goal is: {BFSAP2.goal} .")
                
        drawBtn( Env2,BFSAP2,nodeColors)
    
            
        
    if st.session_state["clicked"]:
        if st.session_state["env"].is_agent_alive(st.session_state["agent"]):
            #st.warning("Agent Step Done!")
            st.success(" Agent is working...")
            drawBtn(st.session_state["env"],st.session_state["agent"], st.session_state["nodeColors"])
       
    
    
    
        
        
        
                
            
    
    
    
    
    
    
if __name__ == '__main__':
    main()