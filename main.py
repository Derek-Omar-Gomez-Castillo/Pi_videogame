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
        self.state = 'Montecarlo'

    def Intro(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.state = 'Montecarlo'

        screen.blit(background_Intro, (0, 0))
        #refactorizar
        #player_group.draw(screen)
        #player_group.update()
        
        pg.display.flip()

    def Montecarlo(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        screen.blit(heart_surface, (600, 300))
        screen.blit(Tierra_image, (600, 300))
        pg.display.flip()

    def Basilea():
        pass

    def Poligonos_regulares():
        pass
    
    def State_manager(self):
        if self.state == 'Intro':
            self.Intro()
        if self.state == 'Montecarlo':
            self.Montecarlo()


pg.init

clock = pg.time.Clock()

screen_width = 1360
screen_height = 768
screen = pg.display.set_mode( (screen_width, screen_height) )
pg.display.set_caption("Las aventuras de Pi")
#pg.mouse.set_visible(False)

background_Intro = pg.image.load("assets/city.png")
Tierra_image = pg.image.load("assets/Tierra_image.png")
player = Player("assets/player/Bot Wheel/charge.png")
player_group = pg.sprite.Group()
player_group.add(player)
game_state = Game_state()
heart_surface = pg.Surface([100,100])
heart_surface.fill((255,255,255))

while True:
    game_state.State_manager()
    clock.tick(60)