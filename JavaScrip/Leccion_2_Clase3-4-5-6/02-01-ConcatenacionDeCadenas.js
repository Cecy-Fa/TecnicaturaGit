;
var nombre = "Andrea";
var apellido = "Farias";
var nombreCompleto = nombre+' '+apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Cecilia'+' '+'Farias';
console.log(nombreCompleto2);
var juntos  = nombre + 219;//lee de izq a derecha siguiendo la cadea lee el numero como str//
console.log(juntos);
juntos = nombre + 78 + 17;
console.log(juntos);
juntos= 78+17 + nombre;
console.log(juntos);

nombre += apellido; //Tercera concatenacion usando operador simplificado
console.log(nombre);

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//Apellido2 ="Peres";una constante no puede ser modificada
console.log(apellido2);

let x, y;//Se pueden crear variables dentro de una misma linea
x = 17, y = 22; //Se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y;//Se asigna el valor de la operacion
console.log(z)

let _1num = 31; //No usar numeros al iniciar una variable
let rompiendo = "rompe"; //no usar palabras reservadas para variables

console.log(_1num)
console.log(rompiendo)