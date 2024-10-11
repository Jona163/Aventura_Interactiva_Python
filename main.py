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

def elegir_personaje():
    """Selección del personaje."""
    imprimir_lento("Elige tu clase de personaje:")
    imprimir_lento("1. Guerrero")
    imprimir_lento("2. Mago")
    imprimir_lento("3. Ladrón\n")

    while True:
        eleccion = input("Escribe 1, 2, o 3: ").strip()
        if eleccion == '1':
            return "Guerrero"
        elif eleccion == '2':
            return "Mago"
        elif eleccion == '3':
            return "Ladrón"
        else:
            imprimir_lento("Por favor, elige una opción válida.\n")

def encuentro_enemigo():
    """Encuentro con un enemigo."""
    enemigos = ["Orco", "Esqueleto", "Lobo", "Goblin"]
    enemigo = random.choice(enemigos)
    imprimir_lento(f"Te has encontrado con un {enemigo}. ¡Prepárate para la batalla!\n")
    return enemigo

def combate(personaje, enemigo):
    """Sistema de combate."""
    vida_personaje = 100
    vida_enemigo = 50


    while vida_personaje > 0 and vida_enemigo > 0:
        imprimir_lento(f"Tu vida: {vida_personaje} | Vida del {enemigo}: {vida_enemigo}\n")
        imprimir_lento("1. Atacar")
        imprimir_lento("2. Huir\n")

        accion = input("Escribe 1 o 2: ").strip()
        if accion == '1':
            danio = random.randint(10, 30)
            imprimir_lento(f"¡Atacas al {enemigo} y le haces {dano} de daño!")
            vida_enemigo -= danio
            if vida_enemigo <= 0:
                imprimir_lento(f"¡Has derrotado al {enemigo}!\n")
                return True
        elif accion == '2':
            imprimir_lento("¡Decides huir como un cobarde!")
            return False
        else:
            imprimir_lento("Opción no válida. El enemigo te golpea mientras dudas.\n")

        danio_enemigo = random.randint(5, 20)
        imprimir_lento(f"El {enemigo} te ataca y te hace {danio_enemigo} de daño.")
        vida_personaje -= danio_enemigo

    if vida_personaje <= 0:
        imprimir_lento("¡Has sido derrotado en batalla!\n")
        return False

def tesoro():
    """Ganar un tesoro tras la victoria."""
    tesoros = ["Espada legendaria", "Poción mágica", "Armadura dorada", "Collar de poder"]
    tesoro_obtenido = random.choice(tesoros)
    imprimir_lento(f"¡Has encontrado un cofre y dentro está un {tesoro_obtenido}!")
    imprimir_lento(f"¡El {tesoro_obtenido} ahora es tuyo!\n")

def main():
    """Función principal que ejecuta el juego."""
    introduccion()
    personaje = elegir_personaje()
    imprimir_lento(f"Has elegido ser un {personaje}. ¡Una excelente elección!\n")

 continuar = True
    while continuar:
        enemigo = encuentro_enemigo()
        resultado = combate(personaje, enemigo)
        if resultado:
            tesoro()
        else:
            imprimir_lento("Te recuperas de la batalla y decides continuar tu aventura otro día...\n")
            continuar = False

    imprimir_lento("Gracias por jugar. ¡Hasta la próxima, valiente aventurero!\n")

#Metodo main
if __name__ == "__main__":
    main()
