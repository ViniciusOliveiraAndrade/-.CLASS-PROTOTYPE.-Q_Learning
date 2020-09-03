class Cell (object):
    def __init__(self, i, j, u=0, terminal=False):
        self.i = i
        self.j = j
        self.u = u
        self.vU = 0
        self.vR = 0
        self.vD = 0
        self.vL = 0
        self.terminal = terminal

    def policy(self):
        action = ["UP", "RIGHT", "DOWN", "LEFT"]
        aux = [self.vU, self.vR, self.vD, self.vL]
        index = 0
        i = 0
        while i < 3:
            if aux[index] < aux[i+1]:
                index = i + 1
            i = i + 1
        return action[index]
    
    def setU(self,valor):
        if valor>self.u:
            self.u = valor
    def setTerminal(self, valor):
        self.terminal = True
        self.u = valor
        self.vU = valor
        self.vD = valor
        self.vL = valor
        self.vR = valor
