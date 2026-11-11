package com.mycompany.rpgmanager;

public class Arquero extends Personaje {

    private int flechas;
    private int precision;

    public Arquero(String nombre, int nivel,
                   int vidaMaxima, int ataque,
                   int flechas, int precision) {

        super(nombre, nivel, vidaMaxima, ataque);

        this.flechas = flechas;
        this.precision = precision;
    }

    @Override
    public String toString() {
        return super.toString()
                + " | Flechas: " + flechas
                + " | Precision: " + precision;
    }
}
