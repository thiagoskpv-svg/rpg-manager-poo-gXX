from personaje import Personaje

class Mago(Personaje):

    def __init__(self, nombre, nivel, vida_maxima,
                 ataque, mana):

        super().__init__(nombre, nivel, vida_maxima, ataque)
        self.mana = mana

    def mostrar_mana(self):
        print(f"{self.nombre} tiene {self.mana} puntos de mana")

    def atacar(self, objetivo, hechizo=None):

        if hechizo is None:
            costo_mana = 10
        else:
            costo_mana = 20

        if self.mana < costo_mana:
            print(f"{self.nombre} no tiene suficiente mana")
            return

        self.mana -= costo_mana

        super().atacar(objetivo)

        if hechizo is not None:
            objetivo.recibir_dano(10)
            print(f"{self.nombre} lanza {hechizo}")

    def __str__(self):
        return super().__str__() + f" | Mana: {self.mana}"
