  /*
 * Ejercicio 3: Leer números hasta que se introduzca un cero.
 * Para cada número, indicar si es par o impar.
 * Clase Scanner 
 */
package Ciclos03;

import java.util.Scanner;

public class Ejercicio03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Ingrese un numero (0 para salir): ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El numero " + numero + " es par");
            }
            else{
                System.out.println("El numero " + numero + " es impar");
            }
            System.out.println("Ingrese otro numero (0 para terminar): ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Finalizaste el programa con " + numero);
    }
    
}