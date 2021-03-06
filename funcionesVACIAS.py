from principal import *
from configuracion import *

import random
import math


def generarPosicion(listaPosiciones,inicio,fin):

    posicion = [] ## guardará x, y
    posicion.append(random.randrange(inicio,fin,10)) ## valor de X
    posicion.append(35) ## valor de Y de primera línea

    # Cambia el valor de x si esta cerca de otra posicion
    i = 0
    while estaCerca(posicion, listaPosiciones):
        posicion[X] = random.randrange(inicio,fin,10)
        i = i + 1
        # Si no encuentra lugar, enviá una posición aunque sea invalida.
        if i > 25:
            return posicion

    return posicion

def separarPalabra(palabra):
    # Prevenimos que la primer columna tenga demasiado peso.
    primerCorte = random.randrange(0, len(palabra)//2)
    segundoCorte = random.randrange(primerCorte, len(palabra))

    cortes = []
    cortes.append(primerCorte)
    cortes.append(segundoCorte)
    return cortes

def borrar(lista,posiciones,indicesBorrar):
    for i in range(len(indicesBorrar)-1,-1,-1):
        indiceBorrar = indicesBorrar[i]
        posiciones.pop(indiceBorrar)
        lista.pop(indiceBorrar)

def tieneEspacio(posiciones):
    # Se asegura de que haya espacio en la primera línea para agregar letras.
    cantidad = 0
    for posicion in posiciones:
        if posicion[Y] == 35:
            cantidad = cantidad + 1
    return cantidad < MAX_LETRA_COLUMNA

def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

    palabra = lista[random.randrange(0, len(lista))]
    cortes = separarPalabra(palabra)

    i = 0
    for letra in palabra:
        if i <= cortes[0] and tieneEspacio(posicionesIzq):
            listaIzq.append(letra)
            posicionesIzq.append(generarPosicion(posicionesIzq,INICIO_IZQ,FIN_IZQ))
        elif i <= cortes[1] and tieneEspacio(posicionesMedio):
            listaMedio.append(letra)
            posicionesMedio.append(generarPosicion(posicionesMedio,INICIO_MED,FIN_MED))
        elif tieneEspacio(posicionesDer):
            listaDer.append(letra)
            posicionesDer.append(generarPosicion(posicionesDer,INICIO_DER,FIN_DER))
        i = i + 1

def bajar(lista, posiciones):
    # hace bajar las letras y elimina las que tocan el piso
    indicesBorrar = []
    for i in range(0,len(posiciones)):
        posicion = posiciones[i]
        nuevoY = posicion[Y]+DISTANCIA_MIN+1
        if nuevoY<(PISO-10):
            posiciones[i] = (posicion[X],nuevoY)
        else:
            indicesBorrar.append(i)
    borrar(lista,posiciones,indicesBorrar)

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    # llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    # Previene que cargarListas se quede sin espacio para cargar más listas
    for i in range(2):
        bajar(listaIzq,posicionesIzq)
        bajar(listaMedio,posicionesMedio)
        bajar(listaDer,posicionesDer)

    # cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    if random.randrange(1,101,1) < 30: # acorta cantidad de palabras que aparecen
        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)

def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos

    # |posicion1 - posicion2| = distancia entre las dos posiciones
    for posicion in lista:
        if abs(elem[X] - posicion[X]) <= DISTANCIA_MIN and abs(elem[Y] - posicion[Y]) <= DISTANCIA_MIN:
            return True
    return False

def Puntos(candidata):
    # devuelve el puntaje que le corresponde a candidata
    vocales = ["a","e","i","o","u"]
    consonDif = ["j","k","q","w","x","y","z"]
    consonFac = ["b","c","d","f","g","h","l","m","n","ñ","p","r","s","t","v"]
    puntos = 0

    puntos = puntos + vecesEnPalabra(vocales, candidata) * VALORVOCAL
    puntos = puntos + vecesEnPalabra(consonDif, candidata) * VALORCONSONDIF
    puntos = puntos + vecesEnPalabra(consonFac, candidata) * VALORCONSONFAC

    return puntos

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    # chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta
    puntos=0
    if esValida(lista, candidata, listaIzq, listaMedio, listaDerecha) == True:
        puntos = Puntos(candidata)
        lista.pop(dondeEsta(lista, candidata))
        sounds("acierto")
    else:
        sounds("fallo")

    return puntos


def esValida(lista, candidata, listaIzq, listaMedio, listaDer):
    # devuelve True si candidata cumple con los requisitos
    if estaEnLista(lista, candidata):
        restoCandidata = candidata
        restoCandidata = acortarCandidata(restoCandidata,listaIzq)
        restoCandidata = acortarCandidata(restoCandidata,listaMedio)
        restoCandidata = acortarCandidata(restoCandidata,listaDer)
        if restoCandidata == "":
            return True
    return False

def acortarCandidata(restoCandidata, lista): ##listaIzq, Med o Der
    restoNuevo = restoCandidata
    # si la primera letra de restoCandidata está en lista, la quitamos
    for caracter in restoCandidata:
        if not estaEnLista(lista,caracter):
            return restoNuevo
        else:
            aux=""
            for i in range(len(restoNuevo)-1,0,-1):
                aux=restoNuevo[i] + aux
            restoNuevo = aux
    return restoNuevo


def estaEnLista(lista, elem_a_buscar):
    for elem in lista:
        if elem == elem_a_buscar:
            return True
    return False

def vecesEnLista(lista, elem_a_buscar):
    cantidad = 0
    for elem in lista:
        if elem == elem_a_buscar:
            cantidad = cantidad + 1
    return cantidad

def vecesEnPalabra(lista, palabra):
    # Toma una palabra y busca la cantidad de elementos de una lista que contiene esta.
    cantidad = 0
    for letra in palabra:
        cantidad = cantidad + vecesEnLista(lista, letra)
    return cantidad

def dondeEsta(lista, elem_a_buscar):
    for i in range(len(lista)):
        if lista[i] == elem_a_buscar:
            return i
    return -1

def sounds(tipo):
    pygame.mixer.init()
    sonidoFallo = pygame.mixer.Sound("Sonidos/fallo.mp3")
    sonidoAcierto = pygame.mixer.Sound("Sonidos/acierto.mp3")
    sonidoFinTiempo = pygame.mixer.Sound("Sonidos/terminoElTiempo.mp3")
    if tipo == "fallo":
        sonidoFallo.play()
    if tipo == "acierto":
        sonidoAcierto.play()
    if tipo == "finTiempo":
        sonidoFinTiempo.play()