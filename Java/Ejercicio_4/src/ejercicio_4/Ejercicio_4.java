package Ejercicio_4;

import java.util.Scanner;

public class Ejercicio_4 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el primer numero: ");
         int numeroA = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el segundo numero: ");
         int numeroB = Integer.parseInt(entrada.nextLine());
    
    var numeroMayor = (numeroA > numeroB)? "Verdadero" : "Falso";
        System.out.println("El numero A es mayor a B?: "+ numeroMayor);
    }
    
}
