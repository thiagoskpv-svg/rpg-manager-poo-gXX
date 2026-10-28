package com.mycompany.rpgmanager;

public class Personaje {

    private String nombre;
    private int nivel;
    private int vida;
    private int vidaMaxima;
    private int ataque;

    public Personaje(String nombre, int nivel,
                     int vidaMaxima, int ataque) {
        this.nombre = nombre;
        this.nivel = nivel;
        this.vidaMaxima = vidaMaxima;
        this.vida = vidaMaxima;
        this.ataque = ataque;
    }

    public int getVida() {
        return vida;
    }

    public void setVida(int valor) {
        this.vida = Math.max(0, Math.min(valor, vidaMaxima));
    }

    public void recibirDano(int cantidad) {
        setVida(vida - cantidad);
    }

    public boolean estaVivo() {
        return vida > 0;
    }

    public void atacar(Personaje objetivo) {
        objetivo.recibirDano(this.ataque);
    }

    @Override
    public String toString() {
        return nombre + " | Nivel: " + nivel
                + " | Vida: " + vida + "/" + vidaMaxima;
    }
}
