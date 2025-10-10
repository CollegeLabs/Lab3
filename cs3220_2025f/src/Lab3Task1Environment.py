from src.problemClass import Problem
from src.graphClass import Graph
from src.environmentClass import Environment

class Task1ProblemGraph(Problem):
    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, state):
        return list(self.graph.origin[state].keys())

    def result(self, state, action):
        return self.graph.origin[state][action]

    def goal_test(self, state):
        super().goal_test(self, state)
    
    def path_cost(self, c, state1, action, state2):
        return c+self.graph.get(state1, state2)
    
class Task1Graph(Graph):
    def __init__(self, graph_dict, locations=None):
        self.origin=graph_dict
        self.graph_dict=dict()
        self.make_graph(graph_dict)
        self.locations=locations
    
    def make_graph(self, graph_dict):
        for a in graph_dict.keys():
            for (act, b) in graph_dict[a].items():
                self.connect(a, b, 1)

    def connect(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance
        #self.graph_dict(A, {})[B] = distance
    
    def nodes(self):
        s1=set([k for k in self.graph_dict.keys()])
        nodes=s1
        return list(nodes)
    
    def get(self, a, b=None):
        links=self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else: 
            return links.get(b)
    
    def getLocation(self, a):
        return self.locations.get(a)
    
#need below to work
    
class Task1Env(Environment):
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
    #Check if agent alive, if so, execute action
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
          if (agent.alive):
            #with agent.state because for PS Agent we don't need to percive
            action=agent.seq.pop(0)
            print("Agent decided to move to {}.".format(action))
            actions.append(action)
          else:
            actions.append("")
            
        for (agent, action) in zip(self.agents, actions):
          self.execute_action(agent, action)
    else:
        print("There is no one here who could work...")