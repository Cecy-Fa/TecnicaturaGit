/*
 Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar
 la suma de todos los números introducidos.
Clase Scanner.
 */
package Ciclos06;

import java.util.Scanner;

public class Ejercicio06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, suma;
        suma = 0;
        System.out.println("Ingrese numeros, para terminar digite 0 (cero)");
        System.out.println("----------------------------------------------------------");
        do { // Usamos el do-while para que al menos se ejecute una vez el ciclo            
            System.out.println("Ingrese un numero: "); // pedimos al usuario un número
            num = Integer.parseInt(entrada.nextLine()); // capturamos el numero con la clase scanner
            if (num != 0) { // Comparamos si el numero es mayor a cero
                suma += num;
            } else {
                System.out.println("Programa finalizado por que ingreso un cero");
                break;
            }   
        } while (num != 0); // el ciclo se va a repetir mientras el numero ingresado no sea cero
        System.out.println("La suma de los nu5"
                + "meros ingresados es: " + suma);
    }
}


