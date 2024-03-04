import pygame as pg, sys
import PI_Funciones
class Sprite(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()
class Player(Sprite):
    def __init__(self, picture_path):
        Sprite.__init__(self, picture_path)
    def update(self):
        self.rect.center = pg.mouse.get_pos()

class Game_state():
    def __init__(self) :
        self.state = 'Intro'

    def Intro(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                     pass
            if event.type == pg.KEYUP:
                if event.key == pg.K_1:
                    self.state = 'Montecarlo'
        pg.display.flip()
        screen.blit(background, (0,0))

    def Montecarlo(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        screen.blit(background, (0, 0))
        player_group.draw(screen)
        player_group.update()
        pg.display.flip()

    def Basilea():
        pass

    def Poligonos_regulares():
        pass
    
    def State_manager(self):
        if self.state == 'Intro':
            self.Intro()
        if self.state == 'Montercalo':
            self.Montecarlo()


pg.init

clock = pg.time.Clock()

screen_width = 1366
screen_height = 768
screen = pg.display.set_mode( (screen_width, screen_height) )
pg.display.set_caption("Las aventuras de Pi")
pg.mouse.set_visible(False)

background = pg.image.load("assets/city.png")
player = Player("assets/player/Bot Wheel/charge.png")
player_group = pg.sprite.Group()
player_group.add(player)
game_state = Game_state()


while True:
    game_state.State_manager()
    clock.tick(60)
