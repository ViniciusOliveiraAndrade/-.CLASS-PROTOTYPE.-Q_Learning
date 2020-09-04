from QLearning import QLearning

# v1

def setup():
    global QL
    size(550, 320)
    QL = QLearning(-1,-10, width, height, 2, 0, rows= 3 , cols = 2, a=0.5, g=0.8)
    
def draw():
    background(51)
    QL.display()
    
def keyTyped():
    if key in ['w','W']:
        QL.up()
    if key in ['d','D']:
        QL.right()
    if key in ['s','S']:
        QL.down()
    if key in ['a','A']:
        QL.left()
    if key == " ":
        QL.auto()
    if key in ['r','R']:
        QL.start()
