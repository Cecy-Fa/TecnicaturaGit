package Ejercicio_5;

import java.util.Scanner;

public class Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float suma, calificacion1, calificacion2, calificacion3;

        System.out.print("Ingrese la primera calificacion: ");
        calificacion1 = Float.parseFloat(entrada.nextLine());

        System.out.print("Ingrese la segunda calificacion: ");
        calificacion2 = Float.parseFloat(entrada.nextLine());

        System.out.print("Ingrese la tercera calificacion: ");
        calificacion3 = Float.parseFloat(entrada.nextLine());

        suma = calificacion1 + calificacion2 + calificacion3;
        System.out.println("La suma es: " + suma);

        entrada.close();
    }
}
