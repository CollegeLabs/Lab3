from src.environmentClass import Environment
from src.graphClass import Graph
from pyvis.network import Network
from src.PS_agentPrograms import BestFirstSearchAgentProgram

class TreasureMapEnv(Environment):
  def __init__(self, navGraph):
    super().__init__()
    self.status = navGraph
    

  def percept(self, agent):
    #Returns the agent's location, and the location status (Dirty/Clean).
    return agent.state

  def is_agent_alive(self, agent):
    return agent.alive

  def update_agent_alive(self, agent):
    if agent.performance <= 0:
      agent.alive = False
      print("Agent {} is dead.".format(agent))
    elif agent.state==agent.goal or len(agent.seq)==0:
      agent.alive = False
      if len(agent.seq)==0:
        print("Agent reached all goals")
      else:
        print(f"Agent reached the goal: {agent.goal}")
      

  def execute_action(self, agent, action):
    '''Check if agent alive, if so, execute action'''
    if self.is_agent_alive(agent):
        """Change agent's location -> agent's state;
        Track performance.
        -1 for each move."""
        agent.state=agent.update_state(agent.state, action)
        agent.performance -= 1
        print(f"Agent in {agent.state} with performance = {agent.performance}")
        self.update_agent_alive(agent)
  
  def step(self):
    if not self.is_done():
        actions = []
        for agent in self.agents:
          if agent.alive:
            #with agent.state because for PS Agent we don't need to percive
            action=agent.seq.pop(0)
            print("Agent decided to do {}.".format(action))
            actions.append(action)
          else:
            actions.append("")
            
        for (agent, action) in zip(self.agents, actions):
          self.execute_action(agent, action)
    else:
        print("There is no one here who could work...")
  
  def Map(Data):
    map = Graph(Data)

    net = Network(heading="Lab3. Treasure Map",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%")   # do this
    
    net.add_nodes(map.nodes(), title=[str(node) for node in map.nodes()])

    nodeColors={
    "start":"red",
    "goal": "green",
    "frontier": "orange",
    "expanded":"pink",
    "Treasure":"yellow"
    }

    for node in net.nodes:
        if node['id']=='Room1':
            node["color"]=nodeColors["start"]
        elif node['id']=='Room48':
            node["color"]=nodeColors["goal"]

    edges=[]
    edges_labels=[]

    for node_source in map.nodes():
        for node_target, dist in map.get(node_source).items():
            if set((node_source,node_target)) not in edges:
                net.add_edge(node_source,node_target, label=str(dist))
                edges.append(set((node_source,node_target)))
                edges_labels.append(str(dist))

    #net.show("graph1.html", notebook=False)

  def Run():
      BFSAP1=BestFirstSearchAgentProgram()

    