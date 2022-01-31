from audioop import reverse
from cgitb import text
import string
from typing import List


class Estado:

    def __init__(self,
                 canibales_Izquierda: int,
                 misioneros_Izquierda: int,
                 canibales_Derecha: int,
                 misioneros_Derecha: int,
                 bote: bool) -> None:

        self.canibales_Izquierda: int = canibales_Izquierda
        self.misioneros_Izquierda: int = misioneros_Izquierda
        self.canibales_Derecha: int = canibales_Derecha
        self.misioneros_Derecha: int = misioneros_Derecha
        # TRUE -> Derecha | FALSE -> Izquierda
        self.bote: bool = bote
        self.explorado: bool = False
        self.padre: Estado = None
        self.hijos: List[Estado] = []

    def GenerarHijos(self):
        hijo: Estado

        if self.bote:
            hijo = Estado(self.canibales_Izquierda,
                          self.misioneros_Izquierda + 1,
                          self.canibales_Derecha,
                          self.misioneros_Derecha - 1,
                          False)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda + 1,
                          self.misioneros_Izquierda,
                          self.canibales_Derecha - 1,
                          self.misioneros_Derecha,
                          False)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda + 1,
                          self.misioneros_Izquierda + 1,
                          self.canibales_Derecha - 1,
                          self.misioneros_Derecha - 1,
                          False)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda,
                          self.misioneros_Izquierda + 2,
                          self.canibales_Derecha,
                          self.misioneros_Derecha - 2,
                          False)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda + 2,
                          self.misioneros_Izquierda,
                          self.canibales_Derecha - 2,
                          self.misioneros_Derecha,
                          False)

            if hijo.EsValido():
                self.hijos.append(hijo)

        else:
            hijo = Estado(self.canibales_Izquierda,
                          self.misioneros_Izquierda - 1,
                          self.canibales_Derecha,
                          self.misioneros_Derecha + 1,
                          True)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda - 1,
                          self.misioneros_Izquierda,
                          self.canibales_Derecha + 1,
                          self.misioneros_Derecha,
                          True)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda - 1,
                          self.misioneros_Izquierda - 1,
                          self.canibales_Derecha + 1,
                          self.misioneros_Derecha + 1,
                          True)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda,
                          self.misioneros_Izquierda - 2,
                          self.canibales_Derecha,
                          self.misioneros_Derecha + 2,
                          True)

            if hijo.EsValido():
                self.hijos.append(hijo)

            hijo = Estado(self.canibales_Izquierda - 2,
                          self.misioneros_Izquierda,
                          self.canibales_Derecha - 2,
                          self.misioneros_Derecha,
                          True)

            if hijo.EsValido():
                self.hijos.append(hijo)

    def EsValido(self) -> bool:
        return ((self.misioneros_Izquierda >= 0 and self.misioneros_Derecha >= 0 and
                 self.canibales_Izquierda >= 0 and self.canibales_Derecha >= 0) and
                (self.misioneros_Izquierda <= 3 and self.misioneros_Derecha <= 3 and
                 self.canibales_Izquierda <= 3 and self.canibales_Derecha <= 3) and
                (self.misioneros_Izquierda == 0 or self.misioneros_Izquierda >= self.canibales_Izquierda) and
                (self.misioneros_Derecha == 0 or self.misioneros_Derecha >= self.canibales_Derecha) and
                (self.bote == True or self.bote == False)
                )

    def EsFinal(self) -> bool:
        return self.canibales_Derecha == 0 and self.misioneros_Derecha == 0

    def ObtenerRecorrido(self) -> string:
        next: Estado = self
        reporte = []
        texto: string = ""
        paso: int = 1

        while (next.padre != None):
            reporte.append(next)
            next = next.padre

        for elemento in reversed(reporte):
            texto += '''Paso {p}
            Canibales izquierda: {cIzquierda}
            Misioneros izquierda: {mIzquierda}
            ------------------------------------
            Canibales derecha: {cDerecha}
            Misioneros derecha: {mDerecha}
            '''.format(p= paso, cIzquierda = elemento.canibales_Izquierda, mIzquierda = elemento.misioneros_Izquierda, cDerecha= elemento.canibales_Derecha, mDerecha= elemento.misioneros_Derecha)

            if elemento.bote:
                texto += "\n Bote: DERECHA"
            else:
                texto += "\n Bote: IZQUIERDA"

            paso += 1

            texto += "\n\n"

        return texto
