from personaje import Personaje

guerrero = Personaje("Guerrero", 5, 100, 25)
monstruo = Personaje("Monstruo", 2, 80, 15)

print("=== INICIO DEL COMBATE ===")

turno = 1

while guerrero.esta_vivo() and monstruo.esta_vivo():

    print(f"\n--- Turno {turno} ---")

    guerrero.atacar(monstruo)
    print(f"Guerrero ataca: {monstruo}")

    if not monstruo.esta_vivo():
        break

    monstruo.atacar(guerrero)
    print(f"Monstruo ataca: {guerrero}")

    turno += 1

print("\n=== FIN DEL COMBATE ===")

from guerrero import Guerrero

thor = Guerrero("Thor", 1, 100, 15, 30, 40)

print("\n=== PRUEBA DE HERENCIA PYTHON ===")
print(thor)
print("¿Thor está vivo?", thor.esta_vivo())


from mago import Mago

mago = Mago("Merlin", 4, 80, 20, 100)

print("\n=== PRUEBA DE HERENCIA: MAGO ===")
print(mago)
mago.mostrar_mana()


from guerrero import Guerrero
from mago import Mago
from arquero import Arquero

print("\n=== RETO 2: HERENCIA ===")

thor = Guerrero("Thor", 5, 100, 25, 30, 40)
merlin = Mago("Merlin", 4, 80, 20, 100)
legolas = Arquero("Legolas", 3, 90, 18, 30, 95)

print(thor)
print(merlin)
print(legolas)

assert thor.esta_vivo()
assert merlin.esta_vivo()
assert legolas.esta_vivo()

print("Pruebas de herencia superadas.")


print("\n=== RETO 3: MAGO Y ARQUERO ===")

objetivo = Personaje("Objetivo", 1, 100, 5)

mago_prueba = Mago("Merlin", 4, 80, 20, 20)
arquero_prueba = Arquero("Legolas", 3, 90, 18, 2, 95)

mago_prueba.atacar(objetivo)
arquero_prueba.atacar(objetivo)

print(mago_prueba)
print(arquero_prueba)
print(objetivo)

assert mago_prueba.mana == 10
assert arquero_prueba.flechas == 1
assert objetivo.vida == 62

print("Pruebas de consumo de recursos superadas.")


print("\n=== RETO 4: SOBRECARGA EN PYTHON ===")

mago_sobrecarga = Mago("Merlin", 4, 80, 20, 30)
objetivo_sobrecarga = Personaje("Objetivo", 1, 100, 5)

mago_sobrecarga.atacar(objetivo_sobrecarga)

assert mago_sobrecarga.mana == 20
assert objetivo_sobrecarga.vida == 80

mago_sobrecarga.atacar(objetivo_sobrecarga, "Bola de fuego")

assert mago_sobrecarga.mana == 0
assert objetivo_sobrecarga.vida == 50

# Comprobar ataque sin mana
mago_sobrecarga.atacar(objetivo_sobrecarga)

assert mago_sobrecarga.mana == 0
assert objetivo_sobrecarga.vida == 50

print(mago_sobrecarga)
print(objetivo_sobrecarga)
print("Pruebas del Reto 4 superadas.")