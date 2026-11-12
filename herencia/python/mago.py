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

    def atacar(self, objetivo):
        costo_mana = 10

        if self.mana >= costo_mana:
            self.mana -= costo_mana
            super().atacar(objetivo)
        else:
            print(f"{self.nombre} no tiene suficiente mana")