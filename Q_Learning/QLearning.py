from Cell import Cell
from UI import UI

class QLearning (object):

    def __init__(self, r, d, ui_width, ui_height, dI, dJ ,rows = 3, cols = 2, a = 0.5, g = 0.8):
        self.r = r
        self.d = d
        self.a = a
        self.g = g
        self.rows = rows
        self.cols = cols
        self.start()
        self.dI = dI
        self.dJ = dJ
        self.i = self.dI
        self.j = self.dJ
        
        self.ui_width=ui_width
        self.ui_height=ui_height
        
        self.ui = UI(ui_width, ui_height)
    
    def start(self):
        self.gridInit()
        self.policyInit()  
                
    def policyInit(self):
        self.policy = []
        for i in range(self.rows):
            self.policy.append([])
            for j in range(self.cols):
                self.policy[i].append("*")
    
    def gridInit(self):
        self.grid = []
        
        self.generateMatriz()
        
        self.grid[0][1].setTerminal(10)

    def generateMatriz(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                cell = Cell(i, j)
                self.grid[i].append(cell)


    # Q(s,a) <- Q(s,a) + alfa[r + gama*max(Q(s+1,a)) - Q(s,a)]
    def up(self):
        cell = self.grid[self.i][self.j]
        
        if cell.terminal:
            self.i = self.dI
            self.j = self.dJ
        else:
            if (self.i-1 <0):
                maxUtility, action = self.max(self.i, self.j)
                u = self.d + (self.g*maxUtility)
                cell.vU = cell.vU + self.a * (u-cell.vU)
                cell.setU(cell.vU)
                self.policy[self.i][self.j] = cell.policy()
            else:
                maxUtility, action = self.max(self.i-1, self.j)
                u = self.r + (self.g*maxUtility)
                cell.vU = cell.vU + self.a * (u-cell.vU)
                cell.setU(cell.vU)
                self.policy[self.i][self.j] = cell.policy()
                self.i= self.i-1
            
            
    def right(self):
        cell = self.grid[self.i][self.j]
        if cell.terminal:
            self.i = self.dI
            self.j = self.dJ
        else:
            if (self.j+1 > self.cols-1):
                cell = self.grid[self.i][self.j]
                maxUtility, action = self.max(self.i, self.j)
                u = self.d + (self.g*maxUtility)
                cell.vR = cell.vR + self.a * (u-cell.vR)
                cell.setU(cell.vR)
                self.policy[self.i][self.j] = cell.policy()
            else:
                maxUtility, action = self.max(self.i, self.j+1)
                u = self.r + (self.g*maxUtility)
                cell.vR = cell.vR + self.a * (u-cell.vR)
                cell.setU(cell.vR)
                self.policy[self.i][self.j] = cell.policy()
                self.j= self.j+1

    def down(self):
        cell = self.grid[self.i][self.j]
        if cell.terminal:
            self.i = self.dI
            self.j = self.dJ
        else:
            if (self.i+1 > self.rows -1):
                maxUtility, action = self.max(self.i, self.j)
                u = self.d + (self.g*maxUtility)
                cell.vD = cell.vD + self.a * (u-cell.vD)
                cell.setU(cell.vD)
                self.policy[self.i][self.j] = cell.policy()
            else:
                maxUtility, action = self.max(self.i+1, self.j)
                u = self.r + (self.g*maxUtility)
                cell.vD = cell.vD + self.a * (u-cell.vD)
                cell.setU(cell.vD)
                self.policy[self.i][self.j] = cell.policy()
                self.i= self.i+1
    
    def left(self):
        cell = self.grid[self.i][self.j]
        if cell.terminal:
            self.i = self.dI
            self.j = self.dJ
        else:
            if (self.j-1 < 0):
                cell = self.grid[self.i][self.j]
                maxUtility, action = self.max(self.i, self.j)
                u = self.d + (self.g*maxUtility)
                cell.vL = cell.vL + self.a * (u-cell.vL)
                cell.setU(cell.vL)
                self.policy[self.i][self.j] = cell.policy()
            else:
                maxUtility, action = self.max(self.i, self.j-1)
                u = self.r + (self.g*maxUtility)
                cell.vL = cell.vL + self.a * (u-cell.vL)
                cell.setU(cell.vL)
                self.policy[self.i][self.j] = cell.policy()
                self.j = self.j-1
        
    def auto(self):
        if self.grid[self.i][self.j].terminal:
            self.i = self.dI
            self.j = self.dJ
        while not self.grid[self.i][self.j].terminal:
            if self.grid[self.i][self.j].policy() == "UP":
                self.up()
            elif self.grid[self.i][self.j].policy() == "RIGHT":
                self.right()
            elif self.grid[self.i][self.j].policy() == "DOWN":
                self.down()
            elif self.grid[self.i][self.j].policy() == "LEFT":
                self.left()
    
    def maxUtility(self, i,j):
        cell = self.grid[i][j]
        if not cell.terminal:
            maxUtility, action = self.max(i, j)
            cell.u = self.r + maxUtility
            self.policy[i][j] = action

    def max(self, i, j):
        cell = self.grid[i][j]
        action = ["UP", "RIGHT", "DOWN", "LEFT"]
        aux = [cell.vU, cell.vR, cell.vD, cell.vL]
        index = 0
        i = 0
        while i < 3:
            if aux[index] < aux[i+1]:
                index = i + 1
            i = i + 1
        return aux[index], action[index]


    def display(self):
        self.ui.display(self.grid, self.policy, self.r, self.a, self.g, self.i, self.j)
