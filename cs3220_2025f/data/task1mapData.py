import random
boatLocations=["Left", "Right"]
objectLocations=["Left", "Boat", "Right"]
actions=["Left", "Right", "Wolf_Load", "Wolf_Unload", "Goat_Load", "Goat_Unload", "Cabbage_Load", "Cabbage_Unload"]

#boat, wolf, goat, cabbage
LLLL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[0], objectLocations[0]))) #0000
LLLB=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[0], objectLocations[1]))) #0001
LLLR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[0], objectLocations[2]))) #0002
LLBL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[1], objectLocations[0]))) #0010
LLBR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[1], objectLocations[2]))) #0012
LLRL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[2], objectLocations[0]))) #0020
LLRB=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[2], objectLocations[1]))) #0021
LLRR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[0], objectLocations[2], objectLocations[2]))) #0022
LBLL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[1], objectLocations[0], objectLocations[0]))) #0100
LBLR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[1], objectLocations[0], objectLocations[2]))) #0102
LBRL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[1], objectLocations[2], objectLocations[0]))) #0120
LBRR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[1], objectLocations[2], objectLocations[2]))) #0122
LRLL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[0], objectLocations[0]))) #0200
LRLB=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[0], objectLocations[1]))) #0201
LRLR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[0], objectLocations[2]))) #0202
LRBL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[1], objectLocations[0]))) #0210
LRBR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[1], objectLocations[2]))) #0212
LRRL=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[2], objectLocations[0]))) #0220
LRRB=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[2], objectLocations[1]))) #0221
LRRR=''.join(map(lambda x: x[0], (boatLocations[0], objectLocations[2], objectLocations[2], objectLocations[2]))) #0222
RLLL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[0], objectLocations[0]))) #1000
RLLB=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[0], objectLocations[1]))) #1001
RLLR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[0], objectLocations[2]))) #1002
RLBL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[1], objectLocations[0]))) #1010
RLBR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[1], objectLocations[2]))) #1012
RLRL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[2], objectLocations[0]))) #1020
RLRB=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[2], objectLocations[1]))) #1012
RLRR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[0], objectLocations[2], objectLocations[2]))) #1022
RBLL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[1], objectLocations[0], objectLocations[0]))) #1100
RBLR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[1], objectLocations[0], objectLocations[2]))) #1102
RBRL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[1], objectLocations[2], objectLocations[0]))) #1120
RBRR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[1], objectLocations[2], objectLocations[2]))) #1122
RRLL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[0], objectLocations[0]))) #1200
RRLB=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[0], objectLocations[1]))) #1201
RRLR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[0], objectLocations[2]))) #1202
RRBL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[1], objectLocations[0]))) #1210
RRBR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[1], objectLocations[2]))) #1212
RRRL=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[2], objectLocations[0]))) #1220
RRRB=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[2], objectLocations[1]))) #1221
RRRR=''.join(map(lambda x: x[0], (boatLocations[1], objectLocations[2], objectLocations[2], objectLocations[2]))) #1222

keylist=[LLLL, LLLB, LLLR, LLBL, LLBR, LLRL, LLRB, LLRR, LBLL, LBLR, LBRL, LBRR, LRLL, LRLB, LRLR, LRBL, LRBR, LRRL, LRRB, LRRR,
         RLLL, RLLB, RLLR, RLBL, RLBR, RLRL, RLRB, RLRR, RBLL, RBLR, RBRL, RBRR, RRLL, RRLB, RRLR, RRBL, RRBR, RRRL, RRRB, RRRR]

task1WorldDicts = dict(
                    LLLL=dict(Right=RLLL, Wolf_Load=LBLL, Goat_Load=LLBL, Cabbage_Load=LLLB),
                    LLLB=dict(Right=RLLB, Cabbage_Unload=LLLL),
                    LLLR=dict(Right=RLLR, Wolf_Load=LBLR, Goat_Load=LLBR),
                    LLBL=dict(Right=RLBL, Goat_Unload=LLLL),
                    LLBR=dict(Right=RLBR, Goat_Unload=LLLR),
                    LLRL=dict(Right=RLRL, Wolf_Load=LBRL, Cabbage_Load=LLRB),
                    LLRB=dict(Right=RLRB, Cabbage_Unload=LLRL),
                    LLRR=dict(Right=RLRR, Wolf_Load=LBRR),
                    LBLL=dict(Right=RBLL, Wolf_Unload=LLLL),
                    LBLR=dict(Right=RBLR, Wolf_Unload=LLLR),
                    LBRL=dict(Right=RBRL, Wolf_Unload=LLRL),
                    LBRR=dict(Right=RBRR, Wolf_Unload=LLRR),
                    LRLL=dict(Right=RRLL, Goat_Load=LRBL, Cabbage_Load=LRLB),
                    LRLB=dict(Right=RRLB, Cabbage_Unload=LRLL),
                    LRLR=dict(Right=RRLR, Goat_Load=LRBR),
                    LRBL=dict(Right=RRBL, Goat_Unload=LRLL),
                    LRBR=dict(Right=RRBR, Goat_Unload=LRLR),
                    LRRL=dict(Right=RRRL, Cabbage_Load=LRRB),
                    LRRB=dict(Right=RRRB, Cabbage_Unload=LRRL),
                    LRRR=dict(Right=RRRR), #should be impossible to reach this scenario, but it's here anyways (only accessable after goal is reached)
                    RLLL=dict(Left=LLLL),
                    RLLB=dict(Left=LLLB, Cabbage_Unload=RLLR),
                    RLLR=dict(Left=LLLR, Cabbage_Load=RLLB),
                    RLBL=dict(Left=LLBL, Goat_Unload=RLRL),
                    RLBR=dict(Left=LLBR, Goat_Unload=RLRR),
                    RLRL=dict(Left=LLRL, Goat_Load=RLBL),
                    RLRB=dict(Left=LLRB, Cabbage_Unload=RLRR),
                    RLRR=dict(Left=LLRR, Goat_Load=RLBR, Cabbage_Load=RLRB),
                    RBLL=dict(Left=LBLL, Wolf_Unload=RRLL),
                    RBLR=dict(Left=LBLR, Wolf_Unload=RRLR),
                    RBRL=dict(Left=LBRL, Wolf_Unload=RRRL),
                    RBRR=dict(Left=LBRR, Wolf_Unload=RRRR),
                    RRLL=dict(Left=LRLL, Wolf_Load=RBLL),
                    RRLB=dict(Left=LRLB, Cabbage_Unload=RRLR),
                    RRLR=dict(Left=LRLR, Wolf_Load=RBLR, Cabbage_Load=RRLB),
                    RRBL=dict(Left=LRBL, Goat_Unload=RRRL),
                    RRBR=dict(Left=LRBR, Goat_Unload=RRRR),
                    RRRL=dict(Left=LRRL, Wolf_Load=RBRL, Goat_Load=RRBL),
                    RRRB=dict(Left=LRRB, Cabbage_Unload=RRRR),
                    RRRR=dict(Left=LRRR, Wolf_Load=RBRR, Goat_Load=RRBR, Cabbage_Load=RRRB))

def Task1Locations(): #puts definitive points on a graph for Task1 (used for pyvis.network)
    x=[]
    y=[]
    n=len(keylist)
    for _ in range(n):
        x.append(random.randint(0, n+1)+100) 
        y.append(random.randint(0, n+1)+100) 
    zipped=zip(x,y)
    return dict(zip(keylist, zipped))