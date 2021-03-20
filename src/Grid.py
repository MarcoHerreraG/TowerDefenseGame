from Cell import Cell 

class Grid:
    def __init__(self):
        self.grid = []
        tam = 55
        posX = 0
        posY = 0
        color = (255, 0, 0)
        for y in range (11):#11
            if color == (255, 0, 0):
                color = (0, 255, 0)
            elif color == (0, 255, 0):
                color = (0, 0, 255)
            elif color == (0, 0, 255):
                color = (255, 0, 0)
            for x in range(18):#18
                id = (x, y)
                posX = x * tam
                posY = y * tam
                '''if (x < 1 and y > 1) or (x > 1 and y < 1):
                    '''
                self.grid.append(Cell(posX, posY, color, tam, id))
                if color == (255, 0, 0):
                    color = (0, 255, 0)
                elif color == (0, 255, 0):
                    color = (0, 0, 255)
                elif color == (0, 0, 255):
                    color = (255, 0, 0)

    def draw(self, screen):
        for cell in self.grid:
            cell.draw(screen)
