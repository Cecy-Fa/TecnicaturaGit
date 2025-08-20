
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        /*System.out.println("Hola mundo desde java")
      
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
         */
        //Var - inferencia de tipos en Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "seguimos estudiando";
        System.out.println("mivariableEntera2 = " + miVariableEntera2);
        System.out.println("mivariablecadena2 = " + miVariableCadena2);
        //soutv + tab
        //Para ejecutar Shift + F6 es la tecla para mayuscula
        //Reglas para definir una variable en Java

        var usuario = "Cecilia";
        var titulo = "Enfermera";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));

        var nombre = "Cecilia";
        System.out.println("\nNueva linea: \n" + nombre); //Diagonal inversa y letra n
        System.out.println("Tabulador: \t" + nombre); //Tabulador un espacio para centrar
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroceso: \b\b"+ nombre); //Caracter de retroceso
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas Dobles: \""+nombre+"\"");*/

        //Clase Scsner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
         */
 /*byte numEnteroByte = (byte)127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:"+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte:"+ Byte.MAX_VALUE);
        
        short numEnteroShort = (short)32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short:"+ Short.MIN_VALUE);
        System.out.println("Valor maximo del Short:"+ Short.MAX_VALUE);
        
        int numEnteroInt = (int)2147483647L;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int:"+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int:"+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long:"+ Long.MIN_VALUE);
        System.out.println("Valor maximo del Long:"+ Long.MAX_VALUE); 
         */

 /*float numFloat = (float)3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de float:" + Float.MIN_VALUE);
        System.out.println("El valor maximo de float:" + Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numdouble = " + numDouble);
        System.out.println("El valor minimo de double:" + Double.MIN_VALUE);
        System.out.println("El valor maximo de double:" + Double.MAX_VALUE);
         */
        //Interferencia de tipos var y tipos primitivos
        /*var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //Automaticamente con el punto decimal se trasforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
         */
        //Tipos primitivos char
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar );
        
        char varCaracter = '\u0024'; //Indicamos a Java la asignacion con el código unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
         char varCaracterSimbolo = '$'; //UN caracter especial, poemos copiar dede unicode
        System.out.println("varCaracterSimbolo = "+ varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; //Indicamos a Java la asignacion con el código unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char) 36; //Valor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //UN caracter especial, poemos copiar dede unicode
        System.out.println("varCaracterSimbolo1 = "+ varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnterochar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);
         */
        //Tipos primitivos Booleanos
        /*boolean varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es verde");
        }
        else {
            System.out.println("La bandera es verde");
        }
        
        //Algoritmo: ¿Es mayor de edad?
        var edad = 18;//Literal tener presente la inferencia de tipos
        //var adulto = edad >= 18; //ESta es una expresión booleana
        if (edad >= 18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }
         */
//        Conversión de tipos primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad + 1));
//        var valorPI = Double.parseDouble("3.1416");
//        System.out.println("valorPI = " +valorPI);
//        
//        //Pedir un valor
//          var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad:");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);
//        
        //Conversión de tipo primitivo en Java Parte 2
        /*var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = "  + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
         */
        //Operadores Aritméticos
        /*int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("Solucion de la suma: = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("Solucion de la resta: = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("Solucion de la multiplicacion: = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("Solucion de la divicion: = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("Solucion2 resultado de la division: " + solucion2);
        
        solucion = num1 % num2;//Guarda el residuo entero de la divicion
        System.out.println("Solucion = " + solucion);
        
        if(num2 % 2 == 0)
            System.out.println("Es un numero Par:");
        else
            System.out.println("Es un numero Impar");
         */
        //Operadores de Asignación
        /* int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;// Una operacion
        System.out.println("varNum3 = " + varNum3);
        
        //Operadores de Composición
        varNum1 += 1; //varNum1 = varNum1 + 1;
        System.out.println("varNum1 = " + varNum1);
        
        //  -=    *=     /=      %=
        varNum2 -= 2; 
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4; 
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6; 
        System.out.println("varNum1 = " + varNum1);
         */
        
        //CLASE 8: Operadores Unarios: Cambio de signo
        
        /*var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);// El resultado será un número negativo

        //Operadores de Negacion/Tipo boolean
        var varC = true; //Esta literal por default en Java es de tipo Boolean
        var varD = !varC; //Aquí esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);

        //Operadores Unarios de Incremento : Preincremento
        var varE = 9; //Se va a modificar su valor
        var varF = ++varE; //Símbolo antes de la variable
        
        //Primero se incrementa la variable y despúes se usa su valor
        System.out.println("varE = " + varE); //Se incrementa en la unidad
        System.out.println("varF = " + varF); //Va a sumar uno

        //Postincremento (el simbolo va despúes de la variable)
        var varG = 3;
        var varH = varG++; //Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);

        //Operadores Unarios de decremento: Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI); //La variable ya esta con decremento
        System.out.println("varJ = " + varJ);
        
        //Operadores Unarios de decremento: Postdecremento
        /*var varK = 8;
        var varL = varK--; //Primero el valor de la variable, luego queda el decremento
        System.out.println("varK = " + varK); //Aqui va a decrementar en I
        System.out.println("varL = " + varL);  
        
        //Operadores de igualdad:
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB; //Comparación de referencia de objeto
        System.out.println("cVar = " + cVar);

        var fVar = cadenaA.equals(cadenaB); //Valor Booleano, comprobando el 
        //contenido de las dos cadenas son iguales
        //Ésta es la forma para comparar  el contenido de los objetos del tipo String
        System.out.println("fVar = " + fVar);

        // Operadores Relacionales:
        var gVar = aNum < bNum; // > < >= >= == !=
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("El numero es par: ");
        } else {
            System.out.println("El numero es Impar");
        }
        var edad = 15;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }
        
        //Operadores Condicionales: AND
        /*var valorA = 7;
        var valorMinimo = 0; //Rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;//reglas establecidas por And
        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        
        //Operadores relacionales: OR
        var vacaciones = true;
        var diaLibre = false;
        if (vacaciones || diaLibre)//Condicional OR
            System.out.println("Papa puede asistir al juego de su hijo");
        else
            System.out.println("Papa no puede asistir al juego de su hijo");
        
        
        //Operador ternario:
        /*var resultadoT = (5 > 8)? "Verdadero": "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "Es Par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);
         */
        
        //Prioridad de los Operadores
        /*var x = 5;
        var y = 10;
        var z = ++x + y--;
        
        System.out.println("x = " + x); //Suma un valor: 6
        System.out.println("y = " + y); // Resta un valor: 9
        System.out.println("z = " + z); // Resultado 16
        
        var solucionAritmetica = 4 + 5 * 6 / 3;//4 + (5 * 6) /3) 
                                               //= 30 / 3 = 10 + 4 = 14 
        System.out.println("solucionaritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3;//4 + 5 = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
         */
        }
