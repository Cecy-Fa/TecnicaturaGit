
//Tipos de datos en JS
/* formatos para escribir comentarios*/
var nombre ="Ceciliaa"; //Dato tipo string(Str)
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000; //Dato tpo numerico
console.log(numero);

//Tipo objeto
var objeto = {
    nombre : "Cecilia",
    apellido : "Farias",
    telefono : "2622-605090"
}
console.log(objeto);

 //Datos de tipo booleanos
var bandera = true;
console.log(bandera);

 //Tipo de dato función
function miFuncion(){}
console.log(typeof miFuncion);

 //Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

 //Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;

    }
}
console.log(typeof Persona);

 //Tipo de dato undefined
var x ;
console.log(typeof x);
x = undefined;
console.log(typeof x);

 //null: significa ausencia de valor
 var y = null; //Null no es un tipo de dato,pero su origen es de tipo object.
console.log(typeof y);

//Tipo de dato array y Empy String
var autos = ['Citroen','Audi','BMW','Ford']; 
console.log(autos);
console.log(typeof autos);//Preguntamos que tipo de dato es y es:

var z = '';
console.log(z);
console.log(typeof z); //ESto se refiere a una cadena vacia