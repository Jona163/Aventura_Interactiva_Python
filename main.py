# Autor: Jonathan Hernández
# Fecha: 10 octubre 2024
# Descripción: Aventura Interactiva en Python.
# GitHub: https://github.com/Jona163

#Importaciones requeridas
import random
import time

def imprimir_lento(texto, retraso=0.04):
    """Imprime el texto lentamente para crear un efecto dramático."""
    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(retraso)
    print()

def introduccion():
    """Introducción del juego."""
    imprimir_lento("¡Bienvenido, valiente aventurero, a las tierras místicas de Pythonia!")
    imprimir_lento("Estás a punto de embarcarte en una búsqueda llena de peligro, misterio y gloria.")
    imprimir_lento("Elige tu camino sabiamente, porque cada decisión dará forma a tu destino.")
    imprimir_lento("Comencemos tu aventura...\n")
    time.sleep(2)
