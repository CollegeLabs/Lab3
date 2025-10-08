from src.problemClass import *

class TreasureMapProblem(Problem):
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. 
    The state space should be included in a subclass
    Then you will create instances of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None, graph=None):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, state):
        return list(self.graph.origin[state].keys())

    def result(self, state, action):
        return self.graph.origin[state][action]

                
