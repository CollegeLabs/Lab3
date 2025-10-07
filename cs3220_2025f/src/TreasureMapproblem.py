from src.problemClass import *

class TreasureMapProblem(Problem):
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. 
    The state space should be included in a subclass
    Then you will create instances of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):

        action = ['Move_Right', 'Move_Left', 'Move_Up', 'Move_Down', 'Grab']

    def result(self, state, action):
        #really not sure what to put here now
        print('Hello World!')

                
