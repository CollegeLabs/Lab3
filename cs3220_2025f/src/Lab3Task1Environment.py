from problemClass import Problem
initState = "LLLL" #boat, wolf, goat, cabbage
goalState = "RRRR"
task1WorldGraph = {"LLLL": {"RLRL": 1}, #all on left -> moving goat across
                   "RLRL": {"LLRL": 1, "LLLL": 1}, #goat and boat on right -> goat on right OR all on left
                   "LLRL": {"RLRR": 1, "RRRL": 1}, #wolf, cabbage, and boat on left -> wolf alone on left
                   "RRRL": {"LLRL": 1, "LRLL": 1},
                   "RLRR": {"LLRL": 1, "LLLR": 1}, #wolf alone on left -> goat alone on left OR cabbage alone on left
                   "LLLR": {"RRLR": 1}, #cabbage alone on right -> goat alone on left
                   "RRLR": {"LRLR": 1, "LLLR": 1, "LRLL": 1}, #goat alone on left -> wolf and cabbage on right
                   "LRLR": {"RRRR": 1, "RRLR": 1}} 
#illegal actions: LRRL, LLRR, RLLR, RRLL, RLLL