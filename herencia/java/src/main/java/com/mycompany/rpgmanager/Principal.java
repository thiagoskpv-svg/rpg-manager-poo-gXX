package com.mycompany.rpgmanager;

public class Principal {

    public static void main(String[] args) {

        Personaje guerrero =
                new Personaje("Guerrero", 5, 100, 25);

        Personaje monstruo =
                new Personaje("Monstruo", 2, 80, 15);

        System.out.println("=== INICIO DEL COMBATE ===");

        int turno = 1;

        while (guerrero.estaVivo() && monstruo.estaVivo()) {

            System.out.println("\n--- Turno " + turno + " ---");

            guerrero.atacar(monstruo);
            System.out.println("Guerrero ataca: " + monstruo);

            if (!monstruo.estaVivo()) {
                break;
            }

            monstruo.atacar(guerrero);
            System.out.println("Monstruo ataca: " + guerrero);

            turno++;
        }

        System.out.println("\n=== FIN DEL COMBATE ===");

        if (guerrero.estaVivo()) {
            System.out.println("Ganador: Guerrero");
        } else {
            System.out.println("Ganador: Monstruo");
        }

        if (guerrero.getVida() < 0 || monstruo.getVida() < 0) {
            throw new AssertionError("La vida es negativa");
        }

        System.out.println(
                "Prueba superada: la vida nunca es negativa."
        );

        System.out.println("\n=== RETO 2: HERENCIA JAVA ===");

        Guerrero thor = new Guerrero(
                "Thor", 5, 100, 25, 30, 40
        );

        Mago merlin = new Mago(
                "Merlin", 4, 80, 20, 100
        );

        Arquero legolas = new Arquero(
                "Legolas", 3, 90, 18, 30, 95
        );

        System.out.println(thor);
        System.out.println(merlin);
        System.out.println(legolas);

        if (!thor.estaVivo()
                || !merlin.estaVivo()
                || !legolas.estaVivo()) {

            throw new AssertionError(
                    "Error: uno de los personajes no esta vivo"
            );
        }

        System.out.println(
                "Pruebas de herencia superadas."
        );
        System.out.println(
                "\n=== RPG MANAGER FINALIZADO CORRECTAMENTE ==="
        );
    }
}

