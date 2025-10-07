from src.problemClass import *

class TreasureMapProblem:
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

        if action == 'Move_Right':
            #agent.location=self.locations[self.locations.index(agent.location)+1]
            location = location(+0,+1)
        elif action == 'Move_Left':
            location = location(+0,-1)
        elif action == 'Move_Up':
            location = location(+1,+0)
        elif action == 'Move_Down':
            location = location(-1,+0)
        """else action == 'Grab':
            change from treasure to normal"""

                
