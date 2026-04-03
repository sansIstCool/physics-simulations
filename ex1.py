import pygame as pg

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

clock = pg.time.Clock()

Circle_x = 200
Circle_y = 200
Radius = 75

vel = 0
gravity = 0.8
jump = -15

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                vel = jump

    vel += gravity
    Circle_y += vel

    if Circle_y > SCREEN_HEIGHT - Radius:
        Circle_y = SCREEN_HEIGHT - Radius
        vel = 0  

    window.fill((30, 30, 30))

    pg.draw.circle(window, (40, 10, 200), (Circle_x, int(Circle_y)), Radius)

    pg.display.flip()
    clock.tick(60)

pg.quit()