import pygame as pg, sys
import PI_Funciones
class Player(pg.sprite.Sprite):
    def __init__(self, width, heigth, position_x, position_y, color):
        super().__init__()
        self.image = pg.Surface([width, heigth])
        self.image.fill(color)
        self.rect = self.image.get_rect()


pg.init

clock = pg.time.Clock()

screen_width = 1366
screen_height = 768
screen = pg.display.set_mode( (screen_width, screen_height) )

player = Player(50, 50, 100, 100,(255, 255, 255))
player_group = pg.sprite.Group()
player_group.add(player)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        

    pg.display.flip()
    player_group.draw(screen)

    clock.tick(60)