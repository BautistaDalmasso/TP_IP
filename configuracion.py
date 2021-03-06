from collections import namedtuple

TAMANNO_LETRA = 20
FPS_inicial = 3
TIEMPO_MAX = 61

ANCHO = 800
ALTO = 600
COLOR_LETRAS = (20,200,20)
COLOR_FONDO = (0,0,0)
COLOR_TEXTO = (200,200,200)
COLOR_TIEMPO_FINAL = (200,20,10)

X = 0
Y = 1

## Extremos de las columnas
INICIO_IZQ=5
FIN_IZQ=250

INICIO_MED=271
FIN_MED=520

INICIO_DER= 537
FIN_DER=787

## Distancia mínima entre letras
DISTANCIA_MIN = 10

## Cantidad máxima de letras por columna
MAX_LETRA_COLUMNA = 9

## Pixel en donde se dibuja el piso
PISO = 527

VALORVOCAL = 1
VALORCONSONFAC = 2
VALORCONSONDIF = 5

PALABRA_SECRETA = "matrix"