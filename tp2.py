"""UCSE - SO II - TP 2

Algoritmos de Reemplazo

* Optimo
* FIFO
* LRU
* Reloj

Integrantes:
    Nombre Apellido <email@dominio.com>
    Nombre Apellido <email@dominio.com>
"""

def print_estado(memoria, fallo, marcas=None, puntero=None):
    """Imprime el estado de la memoria
    """
    # Primera línea: asteriscos (solo para Reloj)
    if marcas is not None:
        asteriscos = ['*' if n else ' ' for n in marcas]
        print("-" * 10)
        print(f"[{', '.join(asteriscos)}]")

    # Segunda línea: memoria y los procesos que la ocupan
    procesos = [str(p) if p is not None else ' ' for p in memoria]
    print(f"[{', '.join(procesos)}]{' F' if fallo else ''}")

    # Tercera línea: puntero (solo para reloj)
    if puntero is not None:
        apuntador = ['|' if n == puntero else ' ' for n in range(len(memoria))]
        print(f"[{', '.join(apuntador)}]")


def optimo(memoria, paginas):
    """Optimo

    >>> optimo([None, None, None, None], [1, 2, 3, 4])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]

    >>> optimo([None, None, None, None], [1, 2, 3, 4, 5, 6, 7, 8])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]
    [5, 2, 3, 4] F
    [5, 6, 3, 4] F
    [5, 6, 7, 4] F
    [5, 6, 7, 8] F

    >>> optimo([None, None, None], [1, 2, 3, 1, 4, 1, 5, 2, 1])
    [1,  ,  ]
    [1, 2,  ]
    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 4] F
    [1, 2, 4]
    [1, 2, 5] F
    [1, 2, 5]
    [1, 2, 5]

    >>> optimo([None, None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]
    [1, 2, 5, 4] F
    [1, 2, 5, 4]
    [1, 2, 5, 4]
    [1, 2, 5, 4]
    [1, 2, 5, 4]

    >>> optimo([None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4, 6, 7, 6, 1])
    [1,  ,  ]
    [1, 2,  ]
    [1, 2,  ]
    [1, 2, 3]
    [1, 2, 4] F
    [1, 2, 5] F
    [1, 2, 5]
    [1, 2, 5]
    [1, 2, 5]
    [1, 4, 5] F
    [1, 4, 6] F
    [1, 7, 6] F
    [1, 7, 6]
    [1, 7, 6]
    """

    fallo = False

    for idx, pagina in enumerate(paginas):

        ## Eliminar comentario y codificar

        print_estado(memoria, fallo)


def fifo(memoria, paginas):
    """FIFO

    >>> fifo([None, None, None, None], [1, 2, 3, 4])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]

    >>> fifo([None, None, None, None], [1, 2, 3, 4, 5, 6, 7, 8])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]
    [5, 2, 3, 4] F
    [5, 6, 3, 4] F
    [5, 6, 7, 4] F
    [5, 6, 7, 8] F

    >>> fifo([None, None, None], [1, 2, 3, 1, 4, 1, 5, 2, 1])
    [1,  ,  ]
    [1, 2,  ]
    [1, 2, 3]
    [1, 2, 3]
    [4, 2, 3] F
    [4, 1, 3] F
    [4, 1, 5] F
    [2, 1, 5] F
    [2, 1, 5]

    >>> fifo([None, None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]
    [5, 2, 3, 4] F
    [5, 2, 3, 4]
    [5, 1, 3, 4] F
    [5, 1, 2, 4] F
    [5, 1, 2, 4]

    >>> fifo([None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4, 6, 7, 6, 1])
    [1,  ,  ]
    [1, 2,  ]
    [1, 2,  ]
    [1, 2, 3]
    [4, 2, 3] F
    [4, 5, 3] F
    [4, 5, 2] F
    [1, 5, 2] F
    [1, 5, 2]
    [1, 4, 2] F
    [1, 4, 6] F
    [7, 4, 6] F
    [7, 4, 6]
    [7, 1, 6] F
    """

    fallo = False

    for idx, pagina in enumerate(paginas):
        i = 0
        while i != len(memoria):
            if memoria[i] == paginas[pagina]:
                origen = 0
                dest = origen + 1
                while origen < len(memoria):
                    if memoria[origen] != None:
                        memoria[dest] = memoria[origen]
                    origen = origen + 1
                    dest = origen + 1
                break
        x = len(memoria) - 1
        while x <= 0:
            if memoria[x] == None:
                origen = len(memoria)
                dest = origen - 1
                while dest >= 0:
                    






        print_estado(memoria, fallo)


def lru(memoria, paginas):
    """LRU

    >>> lru([None, None, None, None], [1, 2, 3, 4])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]

    >>> lru([None, None, None, None], [1, 2, 3, 4, 5, 6, 7, 8])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]
    [5, 2, 3, 4] F
    [5, 6, 3, 4] F
    [5, 6, 7, 4] F
    [5, 6, 7, 8] F

    >>> lru([None, None, None], [1, 2, 3, 1, 4, 1, 5, 2, 1])
    [1,  ,  ]
    [1, 2,  ]
    [1, 2, 3]
    [1, 2, 3]
    [1, 4, 3] F
    [1, 4, 3]
    [1, 4, 5] F
    [1, 2, 5] F
    [1, 2, 5]

    >>> lru([None, None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4])
    [1,  ,  ,  ]
    [1, 2,  ,  ]
    [1, 2,  ,  ]
    [1, 2, 3,  ]
    [1, 2, 3, 4]
    [1, 5, 3, 4] F
    [2, 5, 3, 4] F
    [2, 5, 1, 4] F
    [2, 5, 1, 4]
    [2, 5, 1, 4]

    >>> lru([None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4, 6, 7, 6, 1])
    [1,  ,  ]
    [1, 2,  ]
    [1, 2,  ]
    [1, 2, 3]
    [1, 4, 3] F
    [5, 4, 3] F
    [5, 4, 2] F
    [5, 1, 2] F
    [5, 1, 2]
    [4, 1, 2] F
    [4, 6, 2] F
    [4, 6, 7] F
    [4, 6, 7]
    [1, 6, 7] F
    """

    fallo = False

    for idx, pagina in enumerate(paginas):

        ## Eliminar comentario y codificar

        print_estado(memoria, fallo)


def reloj(memoria, paginas):
    """Reloj

    La salida de este algoritmo consta de 3 líneas:

    Marca sobre los bloques                                 [*,  ,  ]
    Bloques de memoria con los IDs de procesos que los usan [1, 2, 3]
    Posición del apuntador                                  [|,  ,  ]

    Para ese ejemplo, el bloque 0 (el primero) está ocupado por la página 1
    además, dicho bloque está marcado (*) y está siendo apuntado.
    El bloque 1, está ocupado por la página 2 y el bloque 2 por la página 3.

    >>> reloj([None, None, None, None], [1, 2, 3, 4])
    ----------
    [ ,  ,  ,  ]
    [1,  ,  ,  ]
    [ , |,  ,  ]
    ----------
    [ ,  ,  ,  ]
    [1, 2,  ,  ]
    [ ,  , |,  ]
    ----------
    [ ,  ,  ,  ]
    [1, 2, 3,  ]
    [ ,  ,  , |]
    ----------
    [ ,  ,  ,  ]
    [1, 2, 3, 4]
    [|,  ,  ,  ]

    >>> reloj([None, None, None, None], [1, 2, 3, 4, 5, 6, 7, 8])
    ----------
    [ ,  ,  ,  ]
    [1,  ,  ,  ]
    [ , |,  ,  ]
    ----------
    [ ,  ,  ,  ]
    [1, 2,  ,  ]
    [ ,  , |,  ]
    ----------
    [ ,  ,  ,  ]
    [1, 2, 3,  ]
    [ ,  ,  , |]
    ----------
    [ ,  ,  ,  ]
    [1, 2, 3, 4]
    [|,  ,  ,  ]
    ----------
    [ ,  ,  ,  ]
    [5, 2, 3, 4] F
    [ , |,  ,  ]
    ----------
    [ ,  ,  ,  ]
    [5, 6, 3, 4] F
    [ ,  , |,  ]
    ----------
    [ ,  ,  ,  ]
    [5, 6, 7, 4] F
    [ ,  ,  , |]
    ----------
    [ ,  ,  ,  ]
    [5, 6, 7, 8] F
    [|,  ,  ,  ]

    >>> reloj([None, None, None], [1, 2, 3, 1, 4, 1, 5, 2, 1])
    ----------
    [ ,  ,  ]
    [1,  ,  ]
    [ , |,  ]
    ----------
    [ ,  ,  ]
    [1, 2,  ]
    [ ,  , |]
    ----------
    [ ,  ,  ]
    [1, 2, 3]
    [|,  ,  ]
    ----------
    [*,  ,  ]
    [1, 2, 3]
    [|,  ,  ]
    ----------
    [ ,  ,  ]
    [1, 4, 3] F
    [ ,  , |]
    ----------
    [*,  ,  ]
    [1, 4, 3]
    [ ,  , |]
    ----------
    [*,  ,  ]
    [1, 4, 5] F
    [|,  ,  ]
    ----------
    [ ,  ,  ]
    [1, 2, 5] F
    [ ,  , |]
    ----------
    [*,  ,  ]
    [1, 2, 5]
    [ ,  , |]

    >>> reloj([None, None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4])
    ----------
    [ ,  ,  ,  ]
    [1,  ,  ,  ]
    [ , |,  ,  ]
    ----------
    [ ,  ,  ,  ]
    [1, 2,  ,  ]
    [ ,  , |,  ]
    ----------
    [*,  ,  ,  ]
    [1, 2,  ,  ]
    [ ,  , |,  ]
    ----------
    [*,  ,  ,  ]
    [1, 2, 3,  ]
    [ ,  ,  , |]
    ----------
    [*,  ,  ,  ]
    [1, 2, 3, 4]
    [|,  ,  ,  ]
    ----------
    [ ,  ,  ,  ]
    [1, 5, 3, 4] F
    [ ,  , |,  ]
    ----------
    [ ,  ,  ,  ]
    [1, 5, 2, 4] F
    [ ,  ,  , |]
    ----------
    [*,  ,  ,  ]
    [1, 5, 2, 4]
    [ ,  ,  , |]
    ----------
    [*,  , *,  ]
    [1, 5, 2, 4]
    [ ,  ,  , |]
    ----------
    [*,  , *, *]
    [1, 5, 2, 4]
    [ ,  ,  , |]

    >>> reloj([None, None, None], [1, 2, 1, 3, 4, 5, 2, 1, 2, 4, 6, 7, 6, 1])
    ----------
    [ ,  ,  ]
    [1,  ,  ]
    [ , |,  ]
    ----------
    [ ,  ,  ]
    [1, 2,  ]
    [ ,  , |]
    ----------
    [*,  ,  ]
    [1, 2,  ]
    [ ,  , |]
    ----------
    [*,  ,  ]
    [1, 2, 3]
    [|,  ,  ]
    ----------
    [ ,  ,  ]
    [1, 4, 3] F
    [ ,  , |]
    ----------
    [ ,  ,  ]
    [1, 4, 5] F
    [|,  ,  ]
    ----------
    [ ,  ,  ]
    [2, 4, 5] F
    [ , |,  ]
    ----------
    [ ,  ,  ]
    [2, 1, 5] F
    [ ,  , |]
    ----------
    [*,  ,  ]
    [2, 1, 5]
    [ ,  , |]
    ----------
    [*,  ,  ]
    [2, 1, 4] F
    [|,  ,  ]
    ----------
    [ ,  ,  ]
    [2, 6, 4] F
    [ ,  , |]
    ----------
    [ ,  ,  ]
    [2, 6, 7] F
    [|,  ,  ]
    ----------
    [ , *,  ]
    [2, 6, 7]
    [|,  ,  ]
    ----------
    [ , *,  ]
    [1, 6, 7] F
    [ , |,  ]

    """

    fallo = False  # Indica si en ese instante se dió fallo de página
    puntero = 0  # Indica donde está el apuntador (índice de la lista)
    marcas = [0] * len(memoria)  # Indica los bloques de memoria marcados

    for idx, pagina in enumerate(paginas):

        ## Eliminar comentario y codificar

        print_estado(memoria, fallo, marcas, puntero)
