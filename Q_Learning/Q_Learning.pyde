from MDP import MDP

# v1

def setup():
    global mdpA, mdpB, mdpC
    size(550, 320)
    mdpA = MDP(-1,-10, width, height, 2, 0, rows= 3 , cols = 2, number=0, a=0.5, g=0.8)
    
def draw():
    background(51)
    mdpA.display()
    
def keyTyped():
    if key in ['w','W']:
        mdpA.up()
    if key in ['d','D']:
        mdpA.right()
    if key in ['s','S']:
        mdpA.down()
    if key in ['a','A']:
        mdpA.left()
    if key == " ":
        mdpA.auto()
    if key == "r":
        mdpA.start()
