package com.mycompany.rpgmanager;

public class Mago extends Personaje {

    private int mana;

    public Mago(String nombre, int nivel,
                int vidaMaxima, int ataque, int mana) {

        super(nombre, nivel, vidaMaxima, ataque);

        this.mana = mana;
    }

    @Override
    public String toString() {
        return super.toString()
                + " | Mana: " + mana;
    }
}
