import pygame as pg, sys
from pygame.locals import *
import random

pg.init()

s = pg.display.set_mode((800, 800))
pg.display.set_caption("ZHero")
clock = pg.time.Clock()

BG = [70, 50, 100]  # a Tuple is very similar to a List, just the symbol & changeability differ!!!!
WHITE = (255, 255, 255)

def color_generator():
    output = [random.randint(150, 255) for n in range(3)] # try using parenthesis instead of brackets!! see the console
    return output

class ProgressBar:
    def __init__(self, border, p_color, x, y, progress=0):
        self.border = border
        self.p_color = p_color
        self.x = x
        self.y = y
        self.progress = progress

    def draw_bar(self):
        bar_rect = pg.Rect(self.x, self.y, 700, 50)
        pg.draw.rect(s, self.border, bar_rect, 4)
        return bar_rect

    def draw_progress(self):
        pg.draw.rect(s, self.p_color, (self.x+3, self.y+3, self.progress*7-5, 46))

    def collide(self):
        mouse_pos = pg.mouse.get_pos()
        return self.draw_bar().collidepoint(mouse_pos)


bar_list = []
y = 20

while True:
    s.fill(BG)

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_a:
                pbar = ProgressBar(WHITE, color_generator(), 30, y)
                bar_list.append(pbar)
                y += 100

            if e.key == K_d and len(bar_list) > 0:
                bar_list.pop()
                y -= 100

    for bar in bar_list:
        bar.draw_bar()
        bar.draw_progress()
        if bar.collide() and pg.mouse.get_pressed()[0] and bar.progress < 100: bar.progress += 1

    clock.tick(30)
    pg.display.update()
    
