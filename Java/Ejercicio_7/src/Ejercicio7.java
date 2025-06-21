
//Ejercicio_7;

import java.util.Scanner;

//SalarioVendedor

public static void main(String[] args) {
        final int SALARIO_BASE = 1000;
        final int COMISION_POR_CARRO = 150;
        final double PORCENTAJE_VENTA = 0.05;

        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingrese el numero de carros vendidos: ");
        int carrosVendidos = entrada.nextInt();
        
        System.out.print("Ingrese el valor total de las ventas: ");
        double valorVentas = entrada.nextDouble();

        double comisionTotal = (carrosVendidos * COMISION_POR_CARRO) + (valorVentas * PORCENTAJE_VENTA);
        double salarioMensual = SALARIO_BASE + comisionTotal;

        System.out.println("El salario mensual del vendedor es: $" + salarioMensual);
        
    }
