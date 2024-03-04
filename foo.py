import pygame
import math
import random
# Inicializar Pygame
pygame.init()

# Definir colores
Background_color = (11,24,43)
Azul_fuerte = (57,82,170)
Azul_claro = (57,116,178)

# Definir tamaño de la pantalla
ANCHO = 600
ALTO = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Polígono Regular en Pygame")

# Función para dibujar un polígono regular
def dibujar_poligono_regular(surface, color, centro, radio, lados):
    puntos = []
    for i in range(lados):
        angulo = math.radians(360 / lados * i)
        x = centro[0] + radio * math.cos(angulo)
        y = centro[1] + radio * math.sin(angulo)
        puntos.append((x, y))
    pygame.draw.polygon(surface, color, puntos, 2)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Limpiar la pantalla
    pantalla.fill(Background_color)

    # Dibujar polígono regular en el centro de la pantalla
    centro_poligono = (ANCHO // 2, ALTO // 2)
    radio_poligono = 100
    lados_poligono = 7  # Cambiar este valor para dibujar polígonos con diferente número de lados
    dibujar_poligono_regular(pantalla, Azul_fuerte, centro_poligono, radio_poligono, 13)
    dibujar_poligono_regular(pantalla, Azul_claro, centro_poligono, radio_poligono, 12)
    dibujar_poligono_regular(pantalla, (255,255,255), centro_poligono, radio_poligono, 1000)
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
