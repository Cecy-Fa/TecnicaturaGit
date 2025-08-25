package CicloWhile;

public class EjercicioWhile01 {

//Clase 1 CICLOS:
//CICLO WHILE (video 2J)
    public static void main(String[] args) {
        var conteo = 0;//Inferencia de tipos
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable            
        }
 //Ciclo do While (video 3J)
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);
        
//Ciclo for ( video 3J)
        for(var contando = 0; contando <7; contando++){
        //crear unavariable; Condicion; incremento o decremento
        System.out.println("contando = " + contando);
        }
    }
}



