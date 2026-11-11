from personaje import Personaje

class Mago(Personaje):

    def __init__(self, nombre, nivel, vida_maxima,
                 ataque, mana):

        super().__init__(nombre, nivel, vida_maxima, ataque)

        self.mana = mana

    def mostrar_mana(self):
        print(f"{self.nombre} tiene {self.mana} puntos de mana")

    def __str__(self):
        return super().__str__() + f" | Mana: {self.mana}"
