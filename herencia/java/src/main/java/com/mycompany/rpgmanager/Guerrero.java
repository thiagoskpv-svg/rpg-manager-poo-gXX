package com.mycompany.rpgmanager;

public class Guerrero extends Personaje {

    private int fuerza;
    private int armadura;

    public Guerrero(String nombre, int nivel,
                    int vidaMaxima, int ataque,
                    int fuerza, int armadura) {

        super(nombre, nivel, vidaMaxima, ataque);

        this.fuerza = fuerza;
        this.armadura = armadura;
    }

    @Override
    public String toString() {
        return super.toString()
                + " | Fuerza: " + fuerza
                + " | Armadura: " + armadura;
    }
}



