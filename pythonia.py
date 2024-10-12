# Autor: Jonathan Hernández
# Fecha: 11 octubre 2024
# Descripción: Juego simple en Python que simula un encuentro con enemigos
# y la obtención de tesoros. Incluye efectos visuales con colores.
# GitHub: https://github.com/Jona163

#Importacion de librerias a ocupar:
import random
import time

# Colores para la consola
class Color:
    RESET = "\033[0m"
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AZUL = "\033[34m"
    AMARILLO = "\033[33m"
    CIAN = "\033[36m"
    MAGENTA = "\033[35m"
    
def imprimir_lento(texto, retraso=0.04, color=Color.RESET):
    """Imprime el texto lentamente para crear un efecto dramático."""
    for caracter in texto:
        print(color + caracter, end='', flush=True)
        time.sleep(retraso)
    print(Color.RESET)

def introduccion():
    """Introducción del juego."""
    imprimir_lento("¡Bienvenido, valiente aventurero, a las tierras místicas de Pythonia!", color=Color.CIAN)
    imprimir_lento("Estás a punto de embarcarte en una búsqueda llena de peligro, misterio y gloria.", color=Color.CIAN)
    imprimir_lento("Elige tu camino sabiamente, porque cada decisión dará forma a tu destino.", color=Color.CIAN)
    imprimir_lento("Comencemos tu aventura...\n", color=Color.AMARILLO)
    time.sleep(2)
