
class Personaje:
    def __init__(self, nombre, nivel, vida_maxima, ataque):
        self.nombre = nombre
        self.nivel = nivel
        self.vida_maxima = vida_maxima
        self.__vida = vida_maxima
        self.ataque = ataque

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        self.__vida = max(0, min(valor, self.vida_maxima))

    def recibir_dano(self, cantidad):
        self.vida = self.vida - cantidad

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, objetivo):
        objetivo.recibir_dano(self.ataque)

    def __str__(self):
        return f"{self.nombre} | Nivel: {self.nivel} | Vida: {self.vida}/{self.vida_maxima}"





