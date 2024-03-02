import math, random
def metodo_poligonos(numero_lados_poligonos):

    num_lados_poligono = numero_lados_poligonos  # Número de lados del polígono
    radio_circunferencia = 1  # Este es el radio de la circunferencia; el valor de pi no se ve afectado.

    perimetro_inscrito = 4 * math.sqrt(2) * radio_circunferencia
    perimetro_circunscrito = 8 * radio_circunferencia

    num_lados = 4;     # Número de lados de los polígonos con los que estamos trabajando.

    while num_lados * 2 <= num_lados_poligono :  # BUCLE. Si el número de lados del polígono a generar supera el número impuesto por el usuario, para.
            
        perimetro_circunscrito = (2 * perimetro_inscrito * perimetro_circunscrito) / (perimetro_inscrito + perimetro_circunscrito);      # Cálculo de los perímetros con el doble de lados. A cada vuelta los valores de perimetro_inscrito y perimetro_circunscrito se sobreescriben.
        perimetro_inscrito = math.sqrt(perimetro_inscrito * perimetro_circunscrito);        
        num_lados *= 2;              # El número de lados se duplica en cada vuelta.int diametro = num_lados;

    pi = (perimetro_inscrito / 2 / radio_circunferencia + perimetro_circunscrito / 2 / radio_circunferencia) / 2;         # Calculamos pi como la media de los valores de pi de cada perímetro...
    error = (perimetro_inscrito / 2 / radio_circunferencia - perimetro_circunscrito / 2 / radio_circunferencia) / 2;   # ... y el error como la resta.

    print("Con un polígono de ", num_lados, " lados, obtenemos:")
    print("Pi = ", pi, "  +/-  ", error)
    print("Dicho de otra manera, el valor de pi se encuentra entre")
    print(pi + error,  "   y   ", pi - error )

def metodo_monte_carlo():
    num_puntos = 1000000
    num_puntos_circulo = 0
    radio_circunferencia = 1
    for i in range(num_puntos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= radio_circunferencia**2:
            num_puntos_circulo += 1
    pi = 4 * num_puntos_circulo / num_puntos
    print("Con ", num_puntos, " puntos, obtenemos:")
    print("Pi = ", pi)
    

def metodo_brasilea():
    denominador = 1
    valores_fracciones = []
    suma = 0
    for i in range(1, 100000000):
        denominador = i ** 2
        valores_fracciones.append(1/denominador)

    for j in valores_fracciones:
        suma += j
    pi = math.sqrt(6 * suma)
    print(pi)
metodo_brasilea()