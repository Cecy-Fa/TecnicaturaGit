package Ejercicio_3_Rectangulo;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
//Se solicita calcular el área y el perimetro  de un rectangulo
// para estoi deberemos crear las variables:
//alto(int)
//Ancho (int)
//El usuario debe prioporcionar los valores de alto, ancho y despúes
//se debe imprimir el resultado en el siguiente formato:
//Le decimos al usuario:
//Digite el alto del rectácngulo:
//Digite el ancho del rectángulo
//Fórmula:
//ärea = alto * ancho;
//Perímetro = (alto + ancho)*2;
//¿Cuál es el código del ejercicio planteado?

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el alto del rectangulo: ");
        int alto = Integer.parseInt(entrada.nextLine());

        System.out.println("Digite el ancho del rectangulo:");
        int ancho = Integer.parseInt(entrada.nextLine());

        var area = alto * ancho;
        var perimetro = (alto + ancho) * 2;

        System.out.println("Area del rectangulo: " + area);
        System.out.println("El perimetro del rectangulo es: " + perimetro);
        }
    }


    
    

