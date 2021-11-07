import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Life(object):
    def __init__(self, screen, initial_cells):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen
        for i in initial_cells:
            self.pixel(i[0], i[1], WHITE)


    def clear(self):
        self.screen.fill(BLACK)

    def pixel(self, x, y, color):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()
    
    def proximity(self, x, y):
        x-=1
        y-=1
        cont = 0
        sign = 1
        xnum = 1
        ynum = 0
        for i in range(4):
            for j in range(2):
                xcalc=x+j*xnum*sign
                ycalc=y+j*ynum*sign
                if xcalc < 0:
                    xcalc = self.width + xcalc
                elif xcalc >= self.width:
                    xcalc = xcalc % self.width
                if ycalc < 0:
                    ycalc = self.height + ycalc
                elif ycalc >= self.height:
                    ycalc = ycalc % self.height
                if self.prev_turn.get_at((xcalc, ycalc))[:3] == WHITE:
                    cont+=1
            x += xnum*2*sign
            y += ynum*2*sign
            xnum, ynum = ynum, xnum
            if i == 1:
                sign *= -1
        return cont
    
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                p = self.proximity(i,j)
                if self.prev_turn.get_at((i, j))[:3] == WHITE:
                    if p < 2:
                        self.pixel(i, j, BLACK)
                    if p == 2 or p == 3:
                        self.pixel(i, j, WHITE)
                    if p > 3:
                        self.pixel(i, j, BLACK)
                else:
                    if p == 3:
                        self.pixel(i, j, WHITE)


pygame.init()
screen = pygame.display.set_mode((100, 100), pygame.RESIZABLE)
cells = [[25,25], [25,26], [26,26], [26,25],[34,25],[34,26],[34,27],[35,24],[35,28],[36,23],[36,29],[37,23],[37,29], [38,26],[39,28], [39,27], [39,26], [36,27]]
for i in range(2000):
    x = random.randint(0, 120)
    y = random.randint(0, 120)
    cells.append([x,y])
r = Life(screen, cells)
while True:
  pygame.time.delay(100)
  r.copy()
  r.clear()
  r.render()
  pygame.display.flip()