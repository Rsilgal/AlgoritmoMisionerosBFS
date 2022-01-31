from typing import List
from Estado import Estado


class BFS:

    def Busqueda(self, estado_Inicial: Estado):
        actual: Estado
        cola: List[Estado] = [estado_Inicial]

        while len(cola) > 0:
            # actual = cola[0]
            actual = cola.pop(0)

            if actual.EsFinal():
                return actual
            
            actual.GenerarHijos()

            for estado in actual.hijos:
                if not estado.explorado:
                    estado.explorado = True
                    estado.padre = actual
                    cola.append(estado)
