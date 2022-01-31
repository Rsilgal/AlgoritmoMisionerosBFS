from BFS import BFS
from Estado import Estado

# estado: Estado
# busqueda: BFS


def run():
    estado = Estado(0, 0, 3, 3, True)
    busqueda = BFS()
    estadoFinal = busqueda.Busqueda(estado)

    # texto = "Estado Inicial" + "\n"
    # + "Canibales izquierda: " + estado.canibales_Izquierda + "\n"
    # + "Misioneros izquierda: " + estado.misioneros_Izquierda + "\n"
    # + "------------------------" + "\n"
    # + "Canibales derecha: " + estado.canibales_Derecha + "\n"
    # + "Misioneros derecha: " + estado.misioneros_Derecha + "\n"

    texto = '''Estado Inicial:
    Canibales izquierda: {cIzquierda}
    Misioneros izquierda: {mIzquierda}
    ------------------------------------
    Canibales derecha: {cDerecha}
    Misioneros derecha: {mDerecha}
    '''.format(cIzquierda = estado.canibales_Izquierda, mIzquierda = estado.misioneros_Izquierda, cDerecha= estado.canibales_Derecha, mDerecha= estado.misioneros_Derecha)

    print(texto)

    if estado.bote:
        print("Bote: DERECHA")
    else:
        print("Bote: IZQUIERDA")

    print("\n")
    print(estadoFinal.ObtenerRecorrido())


if __name__ == '__main__':
    run()
