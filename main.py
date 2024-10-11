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
