from personaje import Personaje

class Arquero(Personaje):

    def __init__(self, nombre, nivel, vida_maxima,
                 ataque, flechas, precision):

        super().__init__(nombre, nivel, vida_maxima, ataque)

        self.flechas = flechas
        self.precision = precision

    def __str__(self):
        return (super().__str__()
                + f" | Flechas: {self.flechas}"
                + f" | Precision: {self.precision}")
