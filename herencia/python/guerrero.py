from personaje import Personaje

class Guerrero(Personaje):

    def __init__(self, nombre, nivel, vida_maxima,
                 ataque, fuerza, armadura):

        super().__init__(nombre, nivel, vida_maxima, ataque)

        self.fuerza = fuerza
        self.armadura = armadura

    def recibir_dano(self, cantidad):

        # La armadura absorbe el 30% del daño,
        # con un máximo de absorción igual a armadura
        reduccion = min(self.armadura, int(cantidad * 0.30))

        dano_real = max(0, cantidad - reduccion)

        # Delegar al método de Personaje
        super().recibir_dano(dano_real)

    def __str__(self):
        return (super().__str__()
                + f" | Fuerza: {self.fuerza}"
                + f" | Armadura: {self.armadura}")