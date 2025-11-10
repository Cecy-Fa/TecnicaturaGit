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
        
//Palabras break y continue (video 5J)
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break;
            }
        }

        for(var contando = 0; contando <7; contando++){
            if(contando % 2 != 0){
                continue; //Vamos a la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }

//Etiquetas Labels (video 6J) (Ciclos anidados)
inicio:
for(var contando = 0; contando <5; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio;
            }
        }
inicio:
        for(var contando = 0; contando <5; contando++){
            if(contando % 2 != 0){
                continue inicio; //Vamos a la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }
    }   
}



