//Ejercicio para encontrar numeros pares e impares
let parImpar = 10;
if(parImpar % 2 ==0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}
//Ejercicio mayor de edad
let edad = 11, adulto = 18;
if (edad >= adulto ){
    console.log("Es una persona adulta");
}
else{
    console.log("Es una persona menor de dad");
}
//Ejercicio:Dentro de un rango
let dentroRango = 10; //Aca vamos cambiando el valor
let valMin = 0, valMax = 10;
if(dentroRango>= valMin && dentroRango <= valMax){
    console.log("Está dentro del rango establecido")
}
else{
    console.log("Está fuera del rango establecido")
}


//Ejercicio si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if (vacaciones || diaDescanso) {
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre NO puede asistir al juego de su hijo")
}
//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "False";
console.log(resultado2)
let numero = 12;
resultado2 = numero % 2 == 0 ? "Es un numero PAR" : "Es un número IMPAR";
console.log(resultado2);

//Convertir String a number
let miNumero = "21"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); //Esta es una funcion
console.log(typeof edad2);

//Funcion isNaN
if (isNaN(edad2)){//No es un numero - es not a number(devuelve un resultado booleano)
    console.log("Esta variable no contienen solo numero");
}
else{
    if(edad2 >= 18){
        console.log("muy joven para votar")
    }
    else{
        console.log("Puede votar");
    }
}
//Operador ternario
let resultado3 = edad2 >=18? "Puede votar" : "Muy joven para votar"
console.log(resultado3);