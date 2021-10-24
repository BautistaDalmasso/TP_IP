from principal import *
from configuracion import *

import random
import math


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente
    pass


def bajar(lista, posiciones):
    # hace bajar las letras y elimina las que tocan el piso
    pass

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    pass

def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos
    pass

def Puntos(candidata):
    #devuelve el puntaje que le corresponde a candidata
    pass

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta
    pass


def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #devuelve True si candidata cumple con los requisitos
    pass