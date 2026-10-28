package com.mycompany.rpgmanager;

public class Principal {

    public static void main(String[] args) {
        System.out.println("RPG Manager iniciado correctamente");
        Personaje guerrero = new Personaje("Guerrero", 5, 100, 25);
        Personaje monstruo = new Personaje("Monstruo", 2, 80, 15);

        guerrero.atacar(monstruo);

        System.out.println(monstruo);
        System.out.println(monstruo.estaVivo());
    }
}