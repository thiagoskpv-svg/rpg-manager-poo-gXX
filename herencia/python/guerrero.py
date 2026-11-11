from personaje import Personaje

class Guerrero(Personaje):

    def __init__(self, nombre, nivel, vida_maxima,
                 ataque, fuerza, armadura):

        super().__init__(nombre, nivel, vida_maxima, ataque)

        self.fuerza = fuerza
        self.armadura = armadura

    def __str__(self):
        return (super().__str__()
                + f" | Fuerza: {self.fuerza}"
                + f" | Armadura: {self.armadura}")
