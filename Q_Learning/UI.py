class UI(object):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    
    def display(self, grid, policy, r, a, g, ai, aj):
        # Desenha o tabuleiro
        s = 100
        for rows in grid:
            for cell in rows:
                
                x = cell.j * s + 10
                y = cell.i * s + 10
                stroke(255)
                strokeWeight(2)
                fill(100,100,100,100)
                rect(x, y, s, s)
                if cell.terminal:
                    rect(x+6, y+6, s-12, s-12)
                    fill(255,255,255)
                    text("{0:.4f}".format(cell.u), x+(s / 6)+15, y + (s /2) + 4)
                if not cell.terminal:
                    line(x, y, x+s, y+s)
                    line(x+s, y, x, y+s)
                    fill(255,255,255)
                    text("{0:.4f}".format(cell.vL), x+3, y + (s /2) + 4)
                    text("{0:.4f}".format(cell.vR), x+60, y + (s /2) + 4)
                    text("{0:.4f}".format(cell.vU), x+(s / 6) + 15, y + (s /5))
                    text("{0:.4f}".format(cell.vD), x+(s / 6) + 15, y + s - 15)
                    # text("{0:.4f}".format(cell.u), x+(s / 6)+15, y + (s /2) + 4)
                
        
        stroke(0, 102, 255)     
        strokeWeight(3)
        
        # Desenha as informacoes

        half = self.screen_width / 2
        txt = "R= " + str(r) +"\nAlpha= "+str(a)+"\nGama= " +str(g) #+"\nPOLICY: =>"
        fill(255,255,255)
        text(txt, 250 ,  50)
        
        # Desenha a politica
        
        for i in range(3):
            for j in range(2):
                pass
                x_ = (j * s) + (half + 60)
                y_ = (i * s) + 10
                
                stroke(255)
                strokeWeight(2)
                fill(255,255,255,100)
                rect(x_, y_, s, s)
                fill(255,255,255)
                text("{}".format(policy[i][j]), x_+(s / 6), y_ + (s /2))
        
        # Desenha o agente
        noStroke()
        ax = aj * s + 60
        ay = ai * s + 60
        fill(122, 255, 69,200)
        circle(ax, ay, 18)
