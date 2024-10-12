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
    
def elegir_personaje():
    """Selección del personaje."""
    imprimir_lento("Elige tu clase de personaje:", color=Color.AMARILLO)
    imprimir_lento("1. Guerrero", color=Color.VERDE)
    imprimir_lento("2. Mago", color=Color.VERDE)
    imprimir_lento("3. Ladrón\n", color=Color.VERDE)

    while True:
        eleccion = input(Color.AMARILLO + "Escribe 1, 2, o 3: " + Color.RESET).strip()
        if eleccion == '1':
            return "Guerrero"
        elif eleccion == '2':
            return "Mago"
        elif eleccion == '3':
            return "Ladrón"
        else:
            imprimir_lento("Por favor, elige una opción válida.\n", color=Color.ROJO)

def encuentro_enemigo():
    """Encuentro con un enemigo."""
    enemigos = ["Orco", "Esqueleto", "Lobo", "Goblin"]
    enemigo = random.choice(enemigos)
    imprimir_lento(f"Te has encontrado con un {enemigo}. ¡Prepárate para la batalla!\n", color=Color.ROJO)
    return enemigo

def combate(personaje, enemigo):
    """Sistema de combate."""
    vida_personaje = 100
    vida_enemigo = 50

    while vida_personaje > 0 and vida_enemigo > 0:
        imprimir_lento(f"Tu vida: {vida_personaje} | Vida del {enemigo}: {vida_enemigo}\n", color=Color.AZUL)
        imprimir_lento("1. Atacar", color=Color.VERDE)
        imprimir_lento("2. Huir\n", color=Color.VERDE)


        accion = input(Color.AMARILLO + "Escribe 1 o 2: " + Color.RESET).strip()
        if accion == '1':
            dano = random.randint(10, 30)
            imprimir_lento(f"¡Atacas al {enemigo} y le haces {dano} de daño!", color=Color.VERDE)
            vida_enemigo -= dano
            if vida_enemigo <= 0:
                imprimir_lento(f"¡Has derrotado al {enemigo}!\n", color=Color.VERDE)
                return True
       elif accion == '2':
            imprimir_lento("¡Decides huir como un cobarde!", color=Color.ROJO)
            return False
        else:
            imprimir_lento("Opción no válida. El enemigo te golpea mientras dudas.\n", color=Color.ROJO)

        dano_enemigo = random.randint(5, 20)
        imprimir_lento(f"El {enemigo} te ataca y te hace {dano_enemigo} de daño.", color=Color.ROJO)
        vida_personaje -= dano_enemigo
