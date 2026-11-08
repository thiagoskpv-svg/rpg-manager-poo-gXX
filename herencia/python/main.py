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

if guerrero.esta_vivo():
    print("Ganador: Guerrero")
else:
    print("Ganador: Monstruo")

assert guerrero.vida >= 0
assert monstruo.vida >= 0

print("Prueba superada: la vida nunca es negativa.")