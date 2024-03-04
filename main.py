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
                    self.state = 'Intro'
                if event.key == pg.K_2:
                    self.state = 'Montecarlo'
                if event.key == pg.K_3:
                    self.state = 'Basilea'
                if event.key == pg.K_4:
                    self.state = 'Poligonos_regulares'

        screen.blit(background_Intro, (0, 0))
        screen.blit(text1, (center_x+200, center_y-10))
        screen.blit(text2, (center_x+200, center_y+20))        
        screen.blit(text3, (center_x+200, center_y+50))        
        screen.blit(text4, (center_x+200, center_y+80))
        pg.display.flip()

    def Montecarlo(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.state = 'Intro'
                if event.key == pg.K_2:
                    self.state = 'Montecarlo'
                if event.key == pg.K_3:
                    self.state = 'Basilea'
                if event.key == pg.K_4:
                    self.state = 'Poligonos_regulares'
        screen.blit(space_background, (0, 0))
        #screen.blit(heart_surface, (450, 50))
        screen.blit(Tierra_image, (450, 50))
        pg.display.flip()

    def Basilea(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.state = 'Intro'
                if event.key == pg.K_2:
                    self.state = 'Montecarlo'
                if event.key == pg.K_3:
                    self.state = 'Basilea'
                if event.key == pg.K_4:
                    self.state = 'Poligonos_regulares'
        screen.blit(background_Intro, (0, 0))
        pg.display.flip()

    def Poligonos_regulares(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.state = 'Intro'
                if event.key == pg.K_2:
                    self.state = 'Montecarlo'
                if event.key == pg.K_3:
                    self.state = 'Basilea'
                if event.key == pg.K_4:
                    self.state = 'Poligonos_regulares'
        screen.fill(Background_color)
        pg.display.flip()

    def State_manager(self):
        self.dict_states = {'Intro': self.Intro, 'Montecarlo': self.Montecarlo, 'Basilea': self.Basilea, 'Poligonos_regulares': self.Poligonos_regulares}
        self.dict_states[self.state]()


pg.init

clock = pg.time.Clock()

screen_width = 1360
screen_height = 768
screen = pg.display.set_mode( (screen_width, screen_height) )
pg.display.set_caption("Las aventuras de Pi")
pg.font.init()
#pg.mouse.set_visible(False)

#Classes
player = Player("assets/player/Bot Wheel/charge.png")
player_group = pg.sprite.Group()
player_group.add(player)
game_state = Game_state()
#images
background_Intro = pg.image.load("assets/city.png")
Tierra_image = pg.image.load("assets/Tierra_image.png")
Tierra_image = pg.transform.scale(Tierra_image, (500, 500))
heart_surface = pg.Surface([500,500])
heart_surface.fill((218,65,103))
space_background = pg.image.load("assets/Space Background (1).png")
#fonts
font = pg.font.Font(None, 36)
text1 = font.render('Oprime 1 para el Menú de inicio', True, (255, 255, 255))
text2 = font.render('2 para el método de Montecarlo', True, (255, 255, 255))
text3 = font.render('3 para el método de basilea ', True, (255, 255, 255))
text4 = font.render('4 para el método de poligonos regulares', True, (255, 255, 255))
center_x = (screen_width - 1000) // 2
center_y = (screen_height - 26) // 2
Background_color = (11,24,43)

while True:
    game_state.State_manager()
    clock.tick(60)