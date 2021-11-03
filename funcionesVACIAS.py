from principal import *
from configuracion import *

import random
import math



def generarPosicion(listaPosiciones,inicio,fin):

    posicion = [] ## guardará x, y
    posicion.append(random.randrange(inicio,fin,10)) ## valor de X
    posicion.append(35) ## valor de Y de primera línea

    # Cambia el valor de x si esta cerca de otra posicion
    while estaCerca(posicion, listaPosiciones):
        posicion[0] = random.randrange(inicio,fin,10)

    return posicion


def separarPalabra(palabra):
    # Prevenimos que la primer columna tenga demasiado peso.
    primerCorte = random.randrange(0, len(palabra) - len(palabra)//2)
    segundoCorte = random.randrange(primerCorte, len(palabra))

    cortes = []
    cortes.append(primerCorte)
    cortes.append(segundoCorte)
    return cortes


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

    palabra = lista[random.randrange(0, len(lista))]
    cortes = separarPalabra(palabra)

    i = 0

    for letra in palabra:

        if i <= cortes[0]:
            listaIzq.append(letra)
            posicionesIzq.append(generarPosicion(posicionesIzq,INICIO_IZQ,FIN_IZQ))
        elif i <= cortes[1]:
            listaMedio.append(letra)
            posicionesMedio.append(generarPosicion(posicionesMedio,INICIO_MED,FIN_MED))
        else:
            listaDer.append(letra)
            posicionesDer.append(generarPosicion(posicionesDer,INICIO_DER,FIN_DER))
        i = i + 1

def bajar(lista, posiciones):
    # hace bajar las letras y elimina las que tocan el piso
    pass

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    pass

def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos

    # |posicion1 - posicion2| = distancia entre las dos posiciones
    for posicion in lista:
        if abs(elem[0] - posicion[0]) <= DISTANCIA_MIN and abs(elem[1] - posicion[1]) <= DISTANCIA_MIN:
            return True
    return False

def Puntos(candidata):
    #devuelve el puntaje que le corresponde a candidata
    pass

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta
    pass


def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #devuelve True si candidata cumple con los requisitos
    pass





