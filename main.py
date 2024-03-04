import pygame as pg, sys, random, math
import Pi_funciones
class Sprite(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()
class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pg.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pg.transform.scale(image, (scale * width, scale * width))
		image.set_colorkey(colour)

		return image
class Player(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pg.image.load("assets/Crosshair.png")
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pg.mouse.get_pos()
class Ovni(pg.sprite.Sprite):
    def __init__(self, picture_path,pos_x,pos_y):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
    

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
        screen.blit(heart_surface, (450, 100))
        screen.blit(Tierra_image, (450, 100))
        screen.blit(ovni_image, (100, 280))
        
        ovni_group.draw(screen)
        player_group.draw(screen)
        player_group.update()
        
        screen.blit(text_pi_montecarlo, (center_x, 20))

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
        screen.fill(Background_color_poligonos)

        # Dibujar polígono regular en el centro de la pantalla
        centro_poligono = (ANCHO // 2, ALTO // 2)
        radio_poligono = 100
        lados_poligono = 7  # Cambiar este valor para dibujar polígonos con diferente número de lados
        dibujar_poligono_regular(screen, Azul_fuerte, centro_poligono, radio_poligono, 13)
        dibujar_poligono_regular(screen, Azul_claro, centro_poligono, radio_poligono, 12)
        dibujar_poligono_regular(screen, (255,255,255), centro_poligono, radio_poligono, 1000)


        pg.display.flip()

    def State_manager(self):
        self.dict_states = {'Intro': self.Intro, 'Montecarlo': self.Montecarlo, 'Basilea': self.Basilea, 'Poligonos_regulares': self.Poligonos_regulares}
        self.dict_states[self.state]()


pg.init

clock = pg.time.Clock()

screen_width = 1360
screen_height = 768
screen = pg.display.set_mode( (screen_width, screen_height) )
pg.display.set_caption("Las flipantes aventuras de Pi")
pg.font.init()
pg.mouse.set_visible(False)

#game_logic
points_inside = 0

#Classes
ovni = Ovni("assets/ovni.png", 100, 100)
player = Player("assets/Crosshair.png")
player_group = pg.sprite.Group()
player_group.add(player)
game_state = Game_state()
#images
pi_icon = pg.image.load("assets/pi_icon.jpeg")
pg.display.set_icon(pi_icon)
ovni_group = pg.sprite.GroupSingle()
background_Intro = pg.image.load("assets/city.png")
Tierra_image = pg.image.load("assets/Tierra_image.png").convert_alpha()
Tierra_image = pg.transform.scale(Tierra_image, (500, 500))
ovni_image = pg.image.load("assets/ovni.png")
ovni_image = pg.transform.scale(ovni_image, (100, 100))
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
Background_color_poligonos = (11,24,43)
Azul_fuerte = (57,82,170)
Azul_claro = (57,116,178)

# Definir tamaño de la pantalla
ANCHO = 600
ALTO = 600

def dibujar_poligono_regular(surface, color, centro, radio, lados):
    puntos = []
    for i in range(lados):
        angulo = math.radians(360 / lados * i)
        x = centro[0] + radio * math.cos(angulo)
        y = centro[1] + radio * math.sin(angulo)
        puntos.append((x, y))
    pg.draw.polygon(surface, color, puntos, 2)


for i in range(1000):
    new_ovni = Ovni("assets/ovni.png", random.randrange(450, 950), random.randrange(100, 600))
    ovni_group.add(new_ovni)
    points_inside += 1
pi_montecarlo = Pi_funciones.metodo_montecarlo(points_inside)
text_pi_montecarlo = font.render(f"Obtuviste el valor de Pi como: {pi_montecarlo}", True, (255, 255, 255))

while True:
    game_state.State_manager()
    clock.tick(60)