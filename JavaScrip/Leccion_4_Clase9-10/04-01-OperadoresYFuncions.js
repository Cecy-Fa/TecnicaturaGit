//Ejercicio 1: Calcular estaciones del año

let mes = 6;
let estacion; //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "VERANO";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "OTOÑO";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "INVIERNO";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "PRIMAVERA";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estacion: " + estacion);
//Estructura switch(La sintaxis es igual a Java)
switch(mes){//Se pueden usar numeros y cadenas
case 1: case 2: case 12:
    estacion = "VERANO";
    break;
case 3: case 4: case 5:
    estacion = "OTOÑO";
    break;
case 6: case 7: case 8:
    estacion = "INVIERNO";
    break;
case 9: case 10: case 11:
    estacion = "PRIMAVERA";
    break;
    default:
        estacion = "VALOR INCORRECTO";
}
console.log("Bienvenidos a la estación de : "+estacion);

//Ampliando el uso de var,let y const
/*con var puedes reasignar en cualquier momento,
forma parte del ambito global.
Un esrror es que se sobreescriba*/
var nombre = "Andrea";
nombre = "Antonella";
console.log(nombre);

function saludar(){
    var nombre3 = "Abbi";
    console.log(nombre3);
}
//console.log(nombre3); //Aqui no lee el dato en la funcion
if(true){
    var edad = 32;
    console.log(edad);
}
console.log(edad); //En la funcion funciona correctamente,

//Let: funciona en bloque
function saludar2(){
    let nombre2 = "Andrea";
    console.log(nombre2);
}
//console.log(nombre2);
if(true){
    let edad2 = 33;
    console.log(edad2);
}
/*const se utiliza para valores constantes que no pueden ser reasignadas*/
const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//FechaNacimiento = 2003;
//Console.log(fechaNacimiento); //Solo ejecuta el console anterior






//* Ejercicio 2:Horas del día
let hora = 15;
let mensaje;

if (hora >=7 && hora <= 13) {
    mensaje = "Trabajando";
}
else if (hora >13 && hora <=17){
    mensaje = "En casa";
}
else if (hora >17 && hora <=20){
    mensaje = "Escuela de Abbi";
}
else if(hora >20 && hora <=22){
    mensaje = "En casa";
}
else if(hora >22 && hora <=6){
    mensaje = "Descansando...zzz";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje);






//Clase 11: Mejoras de algoritmos con función PARTE 1
/*const se utiliza para valores constantes que no pueden ser reasignadas*/
//Evitar repetir tu codigo//Dry don´t repeat yourself
let days = 1;
switch (days) {
    case 1:
        console.log('HOY ES LUNES');
        break;
    case 2:
        console.log('HOY ES MARTES');
        break;
    case 3:
        console.log('HOY ES MIERCOLES');
        break;
    case 4:
        console.log('HOY ES JUEVES');
        break;
    case 5:
        console.log('HOY ES VIERNES');
        break;
    case 6:
        console.log('HOY ES SABADO');
        break;
    case 7:
        console.log('HOY ES DOMINGO');
        break;
    default:
        console.log("Error en el ingreso del dia de la semana");
        break;
}
//Esta es la opcion mejorada
let days2 = ['LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO','DOMINGO'];
function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(5));


/*Hacer un ejercicio similar al que esta hecho, pero con los menes del año,
hacerlo con estructura switch y luego con la función mejorada*/

switch (3) {
    case 1: 
    mes = "Enero";
        break;
    case 2: 
        mes = "Febrero";
        break;
    case 3: 
        mes = "Marzo";
        break;
    case 4: 
    mes = "Abril";
        break;
    case 5: 
        mes = "Mayo";
        break;
    case 6: 
        mes = "Junio";
        break;
    case 7: 
    mes = "Julio";
        break;
    case 8: 
        mes = "Agosto";
        break;
    case 9: 
        mes = "Septiembres";
        break;
    case 10: 
    mes = "Octubre";
        break;
    case 11: 
        mes = "Noviembre";
        break;
    case 12: 
        mes = "Diciembre";
        break;
    default:
        console.log("Error en el ingreso del dia de la semana")
        break;
}
console.log("Usted esta en el mes de: " + mes);

//Función mejorada
let meses2 = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'];
function getMes(n) {
    if(n < 1 || n > 12){
        throw new Error("FUERA DE RANGO");
    }
    return meses2[n - 1]; // ← Aquí está el acceso correcto al array
}
console.log(getMes(5)); // Debería imprimir "MAYO"

