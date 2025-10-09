from src.problemClass import Problem
from src.graphClass import Graph
from src.navProblemSolvingAgentClass import navProblemSolvingAgent

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
    
