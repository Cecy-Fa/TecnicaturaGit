package Ejercicio_2;

import java.util.Scanner;

public class Ejercicio_2 {
    public static void main(String[] args) {
    // Hacer un programa que calcule e imprima el salario de un empleado
    //a partir de sus horas semanales trabajadas y de su salario por hora 
        
        Scanner sc = new Scanner(System.in);

        int horas;
        double salarioPorHora, salarioSemanal;

        // Solicitar datos al usuario
        System.out.println("Ingrese las horas semanales trabajadas:");
        horas = sc.nextInt();

        System.out.println("Ingrese el salario por hora:");
        salarioPorHora = sc.nextDouble();

        // Calcular salario
        salarioSemanal = horas * salarioPorHora;

        // Mostrar resultado
        System.out.println("El salario semanal del empleado es: $" + salarioSemanal);

        // Cerrar el Scanner
        sc.close();
    }
    
}

    
