/*
 Ejercicio 4: Pedir números hasta que se teclee uno negativo,
 y mostrar cuantos números se han introducido.
 Luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;
import javax.swing.JOptionPane; 

public class Ciclos04 {
    public static void main(String[] args) {
        int num, contador;
        contador = 0;
        System.out.println("Ingrese numeros, para terminar digite un numero negativo");
        System.out.println("----------------------------------------------------------");
        do { // Usamos el do-while para que al menos se ejecute una vez el ciclo            
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));// Pedimos al usuario que ingrese un número usando la clase JOptionPane
            if (num >= 0) { // Comparamos si el numero es mayor o igual a cero
                contador += 1;
            } else { // Si es Negativo, termina el programa
                System.out.println("Programa finalizado por que ingreso un numero negativo");
                break;
            }            
        } while (num >= 0); // el ciclo se va a repetir mientras el numero ingresado es mayor o igual a cero
        System.out.println("Ingreso " + contador + " numeros");
    }    
}
