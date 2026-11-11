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