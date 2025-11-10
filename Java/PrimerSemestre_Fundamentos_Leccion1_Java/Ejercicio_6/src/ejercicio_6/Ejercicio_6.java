package Ejercicio_6;
//Hacer un programa que calcule e imprima la cantidad de dinero 
//que tienen los chicos: Guillermo: N dolares, Luis la mitad de Guillermo
//Juan la mitad de la suma entre Guillermo y Luis

import java.util.Scanner;

public class Ejercicio_6 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo, luis, juan, total;
        System.out.println("Digite la cantidad de dinero que tiene Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo/2;
        juan = (luis + guillermo)/2;
        total = luis + guillermo + juan;
        System.out.println("\nEl dinero que tiene Luis es: U$$" + luis);
        System.out.println("El dinero de Juan es: U$$" + juan);
        System.out.println("El total de dinero entre los 3 es: " + total);

    }

}
