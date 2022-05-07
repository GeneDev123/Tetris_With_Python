# TETRIS
import pygame
import sys
import random

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont("monospace", 25)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
YELLOW = (255, 255, 000)
ORANGE = (255, 128, 0)
PURPLE = (128,0,128)
PINK = (255,182,193)

GRID_COL = (34, 34, 34)

HEIGHT = 600
WIDTH = 450
BOX_SIZE = 30

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIS!")

class grid_point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    occupied = False

class cube():
    def __init__(self, size, type):
        self.size = size
        self.type = type
        self.active = False

        #zigzag1
        if self.type == 1:

            self.color = RED
            self.pos1 = [90, - 30]
            self.pos2 = [120, - 30]
            self.pos3 = [120, - 60]
            self.pos4 = [150, - 60]
            self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        #zigzag2
        elif self.type == 2:
            self.color = GREEN
            self.pos1 = [90, - 60]
            self.pos2 = [120, - 60]
            self.pos3 = [120, - 30]
            self.pos4 = [150, - 30]
            self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        #box
        elif self.type == 3:
            self.color = YELLOW
            self.pos1 = [120, - 60]
            self.pos2 = [120, - 30]
            self.pos3 = [150, - 60]
            self.pos4 = [150, - 30]
            self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        #line
        elif self.type == 4:
            self.color = BLUE
            self.pos1 = [90, - 30]
            self.pos2 = [120, - 30]
            self.pos3 = [150, - 30]
            self.pos4 = [180, - 30]
            self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        #l1
        elif self.type == 5:
            self.color = ORANGE
            self.pos1 = [150, - 90]
            self.pos2 = [150, - 60]
            self.pos3 = [150, - 30]
            self.pos4 = [120, - 30]
            self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        #l2
        elif self.type == 6:
            self.color = PURPLE
            self.pos1 = [120, - 90]
            self.pos2 = [120, - 60]
            self.pos3 = [120, - 30]
            self.pos4 = [150, - 30]
            self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        else:
            self.color = PINK
            self.pos1 = [90, - 30]
            self.pos2 = [120, - 60]
            self.pos3 = [120, - 30]
            self.pos4 = [150, - 30]
            self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

    def change(self):
        if self.type == 1:
            if self.pos1[1] == self.pos2[1]:
                self.pos1[1] -= 30
                self.pos2[0] -= 30
                self.pos3[1] += 30
                self.pos4[0] -= 30
                self.pos4[1] += 60
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            else:
                self.pos1[1] += 30
                self.pos2[0] += 30
                self.pos3[1] -= 30
                self.pos4[0] += 30
                self.pos4[1] -= 60
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        elif self.type == 2:
            if self.pos1[1] == self.pos2[1]:
                self.pos1[0] += 60
                self.pos2[0] += 30
                self.pos2[1] += 30
                self.pos4[0] -= 30
                self.pos4[1] += 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]
            else:
                self.pos1[0] -= 60
                self.pos2[0] -= 30
                self.pos2[1] -= 30
                self.pos4[0] += 30
                self.pos4[1] -= 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]
        elif self.type == 3:
            pass

        elif self.type == 4:
            if self.pos1[1] == self.pos2[1]:
                self.pos1[0] += 60
                self.pos1[1] -= 60
                self.pos2[0] += 30
                self.pos2[1] -= 30
                self.pos4[0] -= 30
                self.pos4[1] += 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]
            else:
                self.pos1[0] -= 60
                self.pos1[1] += 60
                self.pos2[0] -= 30
                self.pos2[1] += 30
                self.pos4[0] += 30
                self.pos4[1] -= 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        elif self.type == 5:
            if self.pos4[1] == self.pos3[1] and self.pos2[1] < self.pos3[1]:
                self.pos1[0] += 30
                self.pos1[1] += 60
                self.pos2[1] += 30
                self.pos3[0] -= 30
                self.pos4[1] -= 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos4[1] < self.pos3[1] and self.pos2[0] < self.pos1[0]:
                self.pos1[0] -= 30
                self.pos2[1] -= 30
                self.pos3[0] += 30
                self.pos3[1] -= 60
                self.pos4[0] += 60
                self.pos4[1] -= 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos3[1] == self.pos4[1] and self.pos3[1] < self.pos2[1]:
                self.pos1[0] -= 30
                self.pos1[1] -= 30
                self.pos3[0] += 30
                self.pos3[1] += 30
                self.pos4[1] += 60
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos1[1] == self.pos2[1] and self.pos3[1] < self.pos4[1]:
                self.pos1[0] += 30
                self.pos1[1] -= 30
                self.pos3[0] -= 30
                self.pos3[1] += 30
                self.pos4[0] -= 60
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        elif self.type == 6:
            if self.pos1[1] < self.pos2[1] and self.pos3[1] == self.pos4[1]:
                self.pos1[0] += 60
                self.pos1[1] += 30
                self.pos2[0] += 30
                self.pos3[1] -= 30
                self.pos4[0] -= 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos3[1] < self.pos4[1] and self.pos1[1] == self.pos2[1]:
                self.pos1[0] -= 30
                self.pos1[1] += 30
                self.pos3[0] += 30
                self.pos3[1] -= 30
                self.pos4[1] -= 60
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos4[1] == self.pos3[1] and self.pos1[1] > self.pos2[1]:
                self.pos1[0] -= 30
                self.pos2[1] += 30
                self.pos3[0] += 30
                self.pos3[1] += 60
                self.pos4[0] += 60
                self.pos4[1] += 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos4[1] < self.pos3[1] and self.pos1[1] == self.pos2[1]:
                self.pos1[1] -= 60
                self.pos2[0] -= 30
                self.pos2[1] -= 30
                self.pos3[0] -= 60
                self.pos4[0] -= 30
                self.pos4[1] += 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

        else:
            if self.pos1[1] == self.pos3[1] and self.pos2[1] < self.pos3[1]:
                self.pos1[1] -= 30
                self.pos3[0] -= 30
                self.pos4[0] -= 60
                self.pos4[1] += 30
                self.pos2[1] += 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos3[1] == self.pos2[1] and self.pos2[0] > self.pos3[0]:
                self.pos4[1] -= 30
                self.pos3[0] += 30
                self.pos1[0] += 60
                self.pos1[1] += 30
                self.pos2[1] += 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos3[0] == self.pos2[0] and self.pos3[1] < self.pos2[1]:
                self.pos2[0] -= 30
                self.pos2[1] -= 30
                self.pos1[0] -= 30
                self.pos1[1] += 30
                self.pos4[0] += 30
                self.pos4[1] -= 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]

            elif self.pos2[1] == self.pos3[1] and self.pos3[0] > self.pos2[0]:
                self.pos1[0] -= 30
                self.pos1[1] -= 30
                self.pos2[0] += 30
                self.pos2[1] -= 30
                self.pos4[0] += 30
                self.pos4[1] += 30
                self.init_composition = [self.pos1, self.pos2, self.pos3, self.pos4]


def downward(active, h, grid_points):
    def chk_height(active, h):
        for i in range(4):
            if active.init_composition[i][1] == h - 30:
                return False
        return True
    move = chk_height(active, h)
    if move:
        active.pos1[1] += 30
        active.pos2[1] += 30
        active.pos3[1] += 30
        active.pos4[1] += 30
        active.init_composition = [active.pos1, active.pos2, active.pos3, active.pos4]
        return False
    else:
        return cube(BOX_SIZE, random.randint(1, 6))
def left(active):
    def chk_left(active):
        for i in range(4):
            if active.init_composition[i][0] == 0:
                return False
        return True
    move = chk_left(active)

    if move:
        active.pos1[0] -= 30
        active.pos2[0] -= 30
        active.pos3[0] -= 30
        active.pos4[0] -= 30
        active.init_composition = [active.pos1, active.pos2, active.pos3, active.pos4]

def right(active, w):
    def chk_right(active, w):
        for i in range(4):
            if active.init_composition[i][0] == w - 180:
                return False
        return True
    move = chk_right(active, w)
    if move:
        active.pos1[0] += 30
        active.pos2[0] += 30
        active.pos3[0] += 30
        active.pos4[0] += 30
        active.init_composition = [active.pos1, active.pos2, active.pos3, active.pos4]


def draw_layout(window, w, h, white, grid):
    pygame.draw.line(window, white, (w - 150, 0), (w - 150, h))
    for hor in range(0, 600, 30):
        pygame.draw.line(window, grid, (0, hor), (w - 150, hor))
    for ver in range(0, 300, 30):
        pygame.draw.line(window, grid, (ver, 0), (ver, 600))

grid_points = []
grid_x = []
grid_y = []
for hor in range(0, 600, 30):
    grid_x.append(hor)
for ver in range(0, 300, 30):
    grid_y.append(ver)
for x in grid_x:
    for y in grid_y:
        grid_points.append(grid_point(x, y))
for i in range(len(grid_points)):
    print(grid_points[i].x, " ",  grid_points[i].y, " ", grid_points[i].occupied)
active = []
active.append(cube(BOX_SIZE, 7))
run = True
while run:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                active[-1].change()
            elif event.key == pygame.K_LEFT:
                left(active[-1])
            elif event.key == pygame.K_RIGHT:
                right(active[-1], WIDTH)
    for i in range(len(active)):
        for draw in range(4):
            pygame.draw.rect(window, active[i].color, (active[i].init_composition[draw][0], active[i].init_composition[draw][1], active[i].size, active[i].size))

    ctr_active = downward(active[-1], HEIGHT, grid_points)
    if ctr_active != False:
        active.append(ctr_active)
    draw_layout(window, WIDTH, HEIGHT, WHITE, GRID_COL)

    title = "TETRIS"
    title_text = my_font.render(title, 1, WHITE)
    window.blit(title_text, (WIDTH - 120, 45))
    clock.tick(5)
    pygame.display.update()