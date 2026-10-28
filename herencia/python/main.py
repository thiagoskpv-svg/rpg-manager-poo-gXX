from personaje import Personaje

guerrero = Personaje("Guerrero", 5, 100, 25)
monstruo = Personaje("Monstruo", 2, 80, 15)

print("=== INICIO DEL COMBATE ===")
print(guerrero)
print(monstruo)

print("\nEl guerrero ataca al monstruo")
guerrero.atacar(monstruo)

print("\n=== DESPUES DEL ATAQUE ===")
print(guerrero)
print(monstruo)

print("\n¿El monstruo sigue vivo?")
print(monstruo.esta_vivo())
