 /*
 Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar
 la suma de todos los números introducidos.
Clase JOptionPane
 */
package Ciclos06;
import javax.swing.JOptionPane;

public class Ciclos06 {
    public static void main(String[] args) {
        int num, suma;
        suma = 0;
        System.out.println("Ingrese numeros, para terminar digite 0 (cero)");
        System.out.println("----------------------------------------------------------");
        do { // Usamos el do-while para que al menos se ejecute una vez el ciclo            
            System.out.println("Ingrese un numero: "); // pedimos al usuario un número
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: ")); // Pedimos al usuario que ingrese un número usando la clase JOptionPane
            if (num != 0) { // Comparamos si el numero es mayor a cero
                suma += num;
            } else {
                System.out.println("Programa finalizado por que ingreso un cero");
                break;
            }   
        } while (num != 0); // el ciclo se va a repetir mientras el numero ingresado no sea cero
        System.out.println("La suma de los numeros ingresados es: " + suma);
    }
}
