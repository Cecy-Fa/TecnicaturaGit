Proceso
Menu_De_Comida
Definir
opcionMenu, opcionCombo, opcionBebida
Como
Entero;
Definir
precioComida, precioBebida
Como
Real;
Definir
nombreCombo, nombreBebida
Como
Cadena;
Definir
numeroTicket, minutosEspera
Como
Entero;
Definir
entrada
Como
Cadena;

opcionMenu < - 0;
opcionCombo < - 0;
opcionBebida < - 0;
precioComida < - 0;
precioBebida < - 0;
nombreCombo < - "";
nombreBebida < - "";

Repetir
Escribir
"===============================";
Escribir
"        MENU PRINCIPAL         ";
Escribir
"===============================";
Escribir
"1. Combos de Hamburguesas";
Escribir
"2. Combos de S�ndwiches";
Escribir
"3. Combos de Pizzas";
Escribir
"4. Personalizar Pedido";
Escribir
"5. Salir";
Escribir
"===============================";

Escribir
"Ingrese una opci�n (1-5):";
Leer
entrada;

Si
entrada = "1"
O
entrada = "2"
O
entrada = "3"
O
entrada = "4"
O
entrada = "5"
Entonces
opcionMenu < - ConvertirANumero(entrada);
Sino
Escribir
"Opci�n inv�lida. Ingrese un n�mero entre 1 y 5.";
opcionMenu < - 0;
Esperar
1.5
Segundos;
FinSi;

Limpiar
Pantalla;
Segun
opcionMenu
Hacer
1:
SeleccionarCombo(1, opcionCombo, precioComida, nombreCombo);
2:
SeleccionarCombo(2, opcionCombo, precioComida, nombreCombo);
3:
SeleccionarCombo(3, opcionCombo, precioComida, nombreCombo);
4:
SeleccionarPersonalizarPedido(nombreBebida, precioBebida);
5:
Escribir
"Gracias por visitar Escuadr�n Lobo. �Hasta pronto!";
FinSegun;

Si
opcionMenu >= 1
Y
opcionMenu <= 3
Entonces

SeleccionarBebida(nombreBebida, precioBebida);

TicketCombos(nombreCombo, nombreBebida, precioComida, precioBebida);

Escribir
"";
Escribir
"�Desea realizar otra compra? (S/N):";
Leer
entrada;
Si
Mayusculas(entrada) <> "S"
Entonces
opcionMenu < - 5;
Sino
Limpiar
Pantalla;
FinSi;
FinSi;

si
opcionMenu = 4
Entonces
Esperar
2
Segundos;
Escribir
"";
Escribir
"�Desea realizar otra compra? (S/N):";
Leer
entrada;
Si
Mayusculas(entrada) <> "S"
Entonces
opcionMenu < - 5;
Sino
Limpiar
Pantalla;
FinSi;
FinSi

Hasta
Que
opcionMenu = 5;

FinProceso

SubProceso
SeleccionarCombo(tipoCombo, opcionCombo
Por
Referencia, precioComida
Por
Referencia, nombreCombo
Por
Referencia)
Definir
entradacombo
Como
caracter;
Definir
validocombo
Como
Logico;
validocombo < - Falso;

Repetir

Segun
tipoCombo
Hacer
1:
Escribir
"===============================";
Escribir
"----- COMBOS DE HAMBURGUESAS -----";
Escribir
"===============================";
Escribir
"1. Combo Cl�sico         - $5.00";
Escribir
"2. Combo BBQ             - $5.50";
Escribir
"3. Combo Doble Carne     - $6.50";
Escribir
"4. Combo Veggie          - $5.25";
Escribir
"5. Combo Picante         - $5.75";
Escribir
"===============================";
2:
Escribir
"===============================";
Escribir
"----- COMBOS DE S�NDWICHES -----";
Escribir
"===============================";
Escribir
"1. Combo Milanesa        - $6.00";
Escribir
"2. Combo Pollo Cl�sico   - $5.75";
Escribir
"3. Combo Club Suprema    - $6.50";
Escribir
"4. Combo Bife de Chorizo - $7.25";
Escribir
"5. Combo Bondiola        - $7.00";
Escribir
"===============================";
3:
Escribir
"===============================";
Escribir
"----- COMBOS DE PIZZAS -----";
Escribir
"===============================";
Escribir
"1. Combo Cl�sico         - $7.00";
Escribir
"2. Combo Napolitano      - $7.50";
Escribir
"3. Combo Familiar        - $10.00";
Escribir
"4. Combo Veggie          - $7.25";
Escribir
"5. Combo Cuatro Quesos   - $8.00";
Escribir
"===============================";
FinSegun;

Escribir
"Seleccione un combo (1-5):";
Leer
entradacombo;

Si
entradacombo = "1"
O
entradacombo = "2"
O
entradacombo = "3"
O
entradacombo = "4"
O
entradacombo = "5"
Entonces
opcionCombo < - ConvertirANumero(entradacombo);
validocombo < - Verdadero;
Sino

validocombo < - Falso;
FinSi;

Segun
tipoCombo
Hacer

1:
Segun
opcionCombo
Hacer
1:
nombreCombo < - "Combo Cl�sico";
precioComida < - 5.00;
2:
nombreCombo < - "Combo BBQ";
precioComida < - 5.50;
3:
nombreCombo < - "Combo Doble Carne";
precioComida < - 6.50;
4:
nombreCombo < - "Combo Veggie";
precioComida < - 5.25;
5:
nombreCombo < - "Combo Picante";
precioComida < - 5.75;
De
Otro
Modo:
Escribir
"Opci�n inv�lida. Intente de nuevo.";
FinSegun;
2:
Segun
opcionCombo
Hacer
1:
nombreCombo < - "Combo Milanesa";
precioComida < - 6.00;
2:
nombreCombo < - "Combo Pollo Cl�sico";
precioComida < - 5.75;
3:
nombreCombo < - "Combo Club Suprema";
precioComida < - 6.50;
4:
nombreCombo < - "Combo Bife de Chorizo";
precioComida < - 7.25;
5:
nombreCombo < - "Combo Bondiola";
precioComida < - 7.00;
De
Otro
Modo:
Escribir
"Opci�n inv�lida. Intente de nuevo.";
FinSegun;
3:
Segun
opcionCombo
Hacer
1:
nombreCombo < - "Combo Cl�sico";
precioComida < - 7.00;
2:
nombreCombo < - "Combo Napolitano";
precioComida < - 7.50;
3:
nombreCombo < - "Combo Familiar";
precioComida < - 10.00;
4:
nombreCombo < - "Combo Veggie";
precioComida < - 7.25;
5:
nombreCombo < - "Combo Cuatro Quesos";
precioComida < - 8.00;
De
Otro
Modo:
Escribir
"Opci�n inv�lida. Intente de nuevo.";
FinSegun;
FinSegun;

Si
validocombo = Falso
Entonces
Esperar
1.5
Segundos;
Limpiar
Pantalla;
FinSi;

Hasta
Que
validocombo = Verdadero;

Limpiar
Pantalla;

FinSubProceso

SubProceso
SeleccionarPersonalizarPedido(nombreBebida, precioBebida)
Definir
tipoComida
Como
Entero;
Definir
tipoCarne
Como
Caracter;
Definir
tipoPan
Como
Cadena;
Definir
tipoIngredientes
Como
Cadena;
Definir
precio
Como
Real;
Definir
precioAcom
Como
Real;
Definir
ensalada, aderezos
Como
Cadena;
Definir
acompanamientoTexto
Como
Cadena;
Definir
tipoMasa, tipoSalsa, tipoQueso, seleccionados
Como
Cadena;
Definir
precioSalsa, precioQueso
Como
Real;
Definir
entradaPer
como
cadena;
precioAcom < - 0;
Precio < - 0;
precioSalsa < - 0;
precioQueso < - 0;

Repetir
Escribir
"===============================";
Escribir
"Seleciona Pedido a personalizar";
Escribir
"===============================";
Escribir
"1. Personalizar Hamburguesas";
Escribir
"2. Personalizar  S�ndwiches";
Escribir
"3. Personalizar  Pizzas";
Escribir
"-------------------------------";
Escribir
"Ingrese una opci�n (1 a 3):";
Leer
entradaPer;

Si
entradaPer = "1"
O
entradaPer = "2"
O
entradaPer = "3"
Entonces
tipoComida < - ConvertirANumero(entradaPer);
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
tipoComida < - 0;
Limpiar
Pantalla;
FinSi;
Hasta
Que
tipoComida >= 1
Y
tipoComida <= 3;

Limpiar
Pantalla;
Segun
tipoComida
Hacer
1:
PersonalizarHamburguesa(precio, tipoPan, tipoCarne);
SeleccionarEnsaladasYAderezos(tipoComida, ensalada, aderezos);
2:
PersonalizarSandwich(tipoPan, tipoCarne, precio); // << < NUEVO
SeleccionarEnsaladasYAderezos(tipoComida, ensalada, aderezos);
3:
PersonalizarPizza(tipoMasa, tipoSalsa, tipoQueso, precioSalsa, precioQueso, seleccionados);
FinSegun;

SeleccionarAcompanamiento(precioAcom, acompanamientoTexto);
SeleccionarBebida(nombreBebida, precioBebida);

Si
tipoComida = 1
O
tipoComida = 2
Entonces
TicketHamburguesaYSandwich(tipoComida, tipoPan, tipoCarne, ensalada, aderezos, acompanamientoTexto, Precio, precioAcom,
                           precioBebida, nombreBebida);
SiNo
TicketPizza(tipoMasa, tipoSalsa, precioSalsa, tipoQueso, precioQueso, seleccionados, acompanamientoTexto, precioAcom,
            precioBebida, nombreBebida);
FinSi

FinSubProceso

SubProceso
PersonalizarHamburguesa(Precio
Por
Referencia, tipoPan
Por
Referencia, tipoCarne
Por
Referencia)
Definir
opcionPan, opcionCarne
Como
Entero;
Definir
entradaHambur
Como
Cadena;
Definir
validoHambur
Como
Logico;

validoHambur < - Falso;

Repetir
Limpiar
Pantalla;
Escribir
"===============================";
Escribir
"   ----- TIPOS DE PAN -----";
Escribir
"===============================";
Escribir
"1. Pan semillas s�samo";
Escribir
"2. Pan brioche";
Escribir
"3. Pan artesanal";
Escribir
"4. Pan integral redondo";
Escribir
"===============================";
Escribir
"Seleccione el tipo de pan (1 a 4):";
Leer
entradaHambur;

Si
entradaHambur = "1"
O
entradaHambur = "2"
O
entradaHambur = "3"
O
entradaHambur = "4"
Entonces
opcionPan < - ConvertirANumero(entradaHambur);
validoHambur < - Verdadero;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
validoHambur < - Falso;
Esperar
1.5
Segundos;
FinSi;

Hasta
Que
validoHambur = Verdadero;

Segun
opcionPan
Hacer
1: tipoPan < - "Pan semillas s�samo";
2: tipoPan < - "Pan brioche";
3: tipoPan < - "Pan artesanal";
4: tipoPan < - "Pan integral redondo";
FinSegun;

validoHambur < - Falso;
Repetir
Limpiar
Pantalla;
Escribir
"===============================";
Escribir
"  ----- TIPOS DE CARNE -----";
Escribir
"===============================";
Escribir
"1. Carne de res     - $5.00";
Escribir
"2. Carne doble      - $6.00";
Escribir
"3. Carne triple     - $7.00";
Escribir
"4. Carne vegana     - $5.50";
Escribir
"===============================";
Escribir
"Seleccione el tipo de carne (1 a 4):";
Leer
entradaHambur;

Si
entradaHambur = "1"
O
entradaHambur = "2"
O
entradaHambur = "3"
O
entradaHambur = "4"
Entonces
opcionCarne < - ConvertirANumero(entradaHambur);
validoHambur < - Verdadero;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
validoHambur < - Falso;
Esperar
1.5
Segundos;
FinSi;

Hasta
Que
validoHambur = Verdadero;

Segun
opcionCarne
Hacer
1:
tipoCarne < - "Carne de res";
Precio < - 5.00;
2:
tipoCarne < - "Carne doble";
Precio < - 6.00;
3:
tipoCarne < - "Carne triple";
Precio < - 7.00;
4:
tipoCarne < - "Carne vegana";
Precio < - 5.50;
FinSegun;

Escribir
"Tipo de pan: ", tipoPan;
Escribir
"Tipo de carne: ", tipoCarne;
Escribir
"Precio total del s�ndwich: $", precio;
Limpiar
Pantalla;
FinSubProceso

SubProceso
PersonalizarSandwich(tipoPan
Por
Referencia, tipoCarne
Por
Referencia, precio
Por
Referencia)
Definir
opcionPan, opcionCarne
Como
Entero;
Definir
respuesta, entradaSand
Como
Cadena;
Definir
validoSand
Como
Logico;

Repetir
Escribir
"===============================";
Escribir
"    Seleccionar tipo de pan:";
Escribir
"===============================";
Escribir
"1. Pan blanco";
Escribir
"2. Pan integral";
Escribir
"3. Pan de centeno";
Escribir
"4. Pan de espelta";
Escribir
"5. Pan de ma�z";
Escribir
"6. Pan de avena";
Escribir
"===============================";
Escribir
"Seleccione una opci�n (1 a 6):";
Leer
entradaSand;

Si
entradaSand = "1"
o
entradaSand = "2"
o
entradaSand = "3"
o
entradaSand = "4"
o
entradaSand = "5"
o
entradaSand = "6"
Entonces
opcionPan < - ConvertirANumero(entradaSand);
validoSand < - Verdadero;
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
validoSand < - Falso;
Limpiar
Pantalla;
FinSi;
Hasta
Que
validoSand = Verdadero

Segun
opcionPan
Hacer
1: tipoPan < - "Pan blanco";
2: tipoPan < - "Pan integral";
3: tipoPan < - "Pan de centeno";
4: tipoPan < - "Pan de espelta";
5: tipoPan < - "Pan de ma�z";
6: tipoPan < - "Pan de avena";
FinSegun;

Repetir
Escribir
"===============================";
Escribir
"  Seleccione tipo de carne:";
Escribir
"===============================";
Escribir
"1. Carnes Calientes";
Escribir
"2. Carnes Fr�as";
Escribir
"===============================";
Escribir
"Ingrese opci�n (1 o 2):";
Leer
respuesta;

Si
respuesta = "1"
O
respuesta = "2"
Entonces
validoSand < - Verdadero;
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
validoSand < - Falso;
Limpiar
Pantalla;
FinSi;
Hasta
Que
validoSand = Verdadero

Si
respuesta = "1"
Entonces
Repetir
Escribir
"===============================";
Escribir
"     Escoja Tipo de carne:";
Escribir
"===============================";
Escribir
"1. Milanesa           $6.00";
Escribir
"2. Suprema            $6.50";
Escribir
"3. Bife de chorizo    $7.00";
Escribir
"4. Bondiola           $7.25";
Escribir
"===============================";
Escribir
"Seleccione una opci�n (1 a 4):";
Leer
entradaSand;

Si
entradaSand = "1"
O
entradaSand = "2"
O
entradaSand = "3"
O
entradaSand = "4"
Entonces
opcionCarne < - ConvertirANumero(entradaSand);
validoSand < - Verdadero;
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
validoSand < - Falso;
Limpiar
Pantalla;
FinSi;
Hasta
Que
validoSand = Verdadero

Segun
opcionCarne
Hacer
1: tipoCarne < - "Milanesa";
Precio < - 6.00;
2: tipoCarne < - "Suprema";
Precio < - 6.50;
3: tipoCarne < - "Bife de chorizo";
Precio < - 7.00;
4: tipoCarne < - "Bondiola";
Precio < - 7.25;
FinSegun;

Sino
Repetir
Escribir
"===============================";
Escribir
"     Escoja Tipo de carne:";
Escribir
"===============================";
Escribir
"1. Jam�n             $5.50";
Escribir
"2. Queso             $5.25";
Escribir
"3. Mortadela         $5.75";
Escribir
"4. Salame            $6.00";
Escribir
"5. Ternera           $6.50";
Escribir
"===============================";
Escribir
"Seleccione una opci�n (1 a 5):";
Leer
entradaSand;

Si
entradaSand = "1"
O
entradaSand = "2"
O
entradaSand = "3"
O
entradaSand = "4"
o
entradaSand = "5"
Entonces
opcionCarne < - ConvertirANumero(entradaSand);
validoSand < - Verdadero;
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
validoSand < - Falso;
Limpiar
Pantalla;
FinSi;
Hasta
Que
validoSand = Verdadero

Segun
opcionCarne
Hacer
1: tipoCarne < - "Jam�n";
Precio < - 5.50;
2: tipoCarne < - "Queso";
Precio < - 5.25;
3: tipoCarne < - "Mortadela";
Precio < - 5.75;
4: tipoCarne < - "Salame";
Precio < - 6.00;
5: tipoCarne < - "Ternera";
Precio < - 6.50;
FinSegun;
FinSi;

Escribir
"Tipo de pan: ", tipoPan;
Escribir
"Tipo de carne: ", tipoCarne;
Escribir
"Precio total del s�ndwich: $", precio;
Limpiar
Pantalla;
FinSubProceso

SubProceso
PersonalizarPizza(tipoMasa
Por
Referencia, tipoSalsa
Por
Referencia, tipoQueso
Por
Referencia, precioSalsa
Por
Referencia, precioQueso
Por
Referencia, seleccionados
Por
Referencia)
Definir
opcionpizza
como
entero;
Definir
entradaPizza
Como
Cadena;
Definir
validoPizza
Como
Logico;
Definir
respuesta, ingrediente
Como
Cadena;
Definir
i
Como
Entero;
Definir
ingredientesCarnesVerduras
Como
Caracter;
Dimension
ingredientesCarnesVerduras[8];

seleccionados < - "";

Repetir
Limpiar
Pantalla;
Escribir
"===============================";
Escribir
"     --- TIPOS DE MASA ---";
Escribir
"===============================";
Escribir
"1. Masa delgada";
Escribir
"2. Masa gruesa";
Escribir
"3. Masa rellena de queso";
Escribir
"===============================";
Escribir
"Seleccione una opci�n (1 a 3):";
Leer
entradaPizza;

Si
entradaPizza = "1"
o
entradaPizza = "2"
o
entradaPizza = "3"
Entonces
opcionpizza < - ConvertirANumero(entradaPizza);
validoPizza < - Verdadero;
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
validoPizza < - Falso;
Limpiar
Pantalla;
FinSi;
Hasta
Que
validoPizza = Verdadero

Segun
opcionpizza
Hacer
1: tipoMasa < - "Masa delgada";
2: tipoMasa < - "Masa gruesa";
3: tipoMasa < - "Masa rellena de queso";
FinSegun;
Escribir
"tipo masa es:", tipoMasa;
Limpiar
Pantalla;

Repetir
Escribir
"===============================";
Escribir
"   Seleccione el tipo de salsa:";
Escribir
"===============================";
Escribir
"1. Salsa tomate cl�sica - $5.00";
Escribir
"2. Salsa barbacoa       - $6.00";
Escribir
"3. Salsa blanca         - $5.50";
Escribir
"4. Pesto                - $7.00";
Escribir
"5. Salsa picante        - $6.50";
Escribir
"===============================";
Escribir
"Seleccione una opci�n (1 a 5):";
Leer
entradaPizza;

Si
entradaPizza = "1"
o
entradaPizza = "2"
o
entradaPizza = "3"
o
entradaPizza = "4"
o
entradaPizza = "5"
Entonces
opcionpizza < - ConvertirANumero(entradaPizza);
validoPizza < - Verdadero;
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
validoPizza < - Falso;
Limpiar
Pantalla;
FinSi;
Hasta
Que
validoPizza = Verdadero

Segun
opcionpizza
Hacer
1:
tipoSalsa < - "Salsa de tomate cl�sica";
precioSalsa < - 5.00;
2:
tipoSalsa < - "Salsa barbacoa";
precioSalsa < - 6.00;
3:
tipoSalsa < - "Salsa blanca";
precioSalsa < - 5.50;
4:
tipoSalsa < - "Pesto";
precioSalsa < - 7.00;
5:
tipoSalsa < - "Salsa picante";
precioSalsa < - 6.50;
FinSegun;

Escribir
"Ha seleccionado: ", tipoSalsa;
Escribir
"Precio: $", precioSalsa;
Limpiar
Pantalla;
Repetir
Escribir
"===============================";
Escribir
"    Seleccione el tipo de queso:";
Escribir
"===============================";
Escribir
"1. Mozzarella     - $4.00";
Escribir
"2. Cheddar        - $4.50";
Escribir
"3. Parmesano      - $5.00";
Escribir
"4. Provolone      - $4.75";
Escribir
"5. Ricotta        - $5.25";
Escribir
"6. Queso vegano   - $6.00";
Escribir
"===============================";
Escribir
"Seleccione una opci�n (1 a 6):";
Leer
entradaPizza;

Si
entradaPizza = "1"
o
entradaPizza = "2"
o
entradaPizza = "3"
o
entradaPizza = "4"
o
entradaPizza = "5"
o
entradaPizza = "6"
Entonces
opcionpizza < - ConvertirANumero(entradaPizza);
validoPizza < - Verdadero;
Limpiar
Pantalla;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
validoPizza < - Falso;
Limpiar
Pantalla;
FinSi;
Hasta
Que
validoPizza = Verdadero

Segun
opcionpizza
Hacer
1:
tipoQueso < - "Mozzarella";
precioQueso < - 2.00;
2:
tipoQueso < - "Cheddar";
precioQueso < - 2.50;
3:
tipoQueso < - "Parmesano";
precioQueso < - 2.00;
4:
tipoQueso < - "Provolone";
precioQueso < - 2.75;
5:
tipoQueso < - "Ricotta";
precioQueso < - 2.25;
6:
tipoQueso < - "Queso vegano";
precioQueso < - 2.00;
FinSegun;

Escribir
"Ha seleccionado: ", tipoQueso;
Escribir
"Precio: $", precioQueso;
Limpiar
Pantalla;

ingredientesCarnesVerduras[0] < - "Jam�n";
ingredientesCarnesVerduras[1] < - "Pepporoni";
ingredientesCarnesVerduras[2] < - "Tocino";
ingredientesCarnesVerduras[3] < - "Salchicha italiana";
ingredientesCarnesVerduras[4] < - "Champi�ones";
ingredientesCarnesVerduras[5] < - "Cebolla";
ingredientesCarnesVerduras[6] < - "Pimientos";
ingredientesCarnesVerduras[7] < - "Espinaca";

Para
i < - 0
Hasta
7
Hacer
ingrediente < - ingredientesCarnesVerduras[i];
Escribir
"===============================";
Escribir
"    Seleciona Ingredientes ";
Escribir
"===============================";
Escribir
"�Desea ", ingrediente, "? (S/N):";
Leer
respuesta;
Limpiar
Pantalla;
Si
Mayusculas(respuesta) = "S"
Entonces
seleccionados < - Concatenar(seleccionados, Concatenar(ingrediente, ", "));
FinSi;
FinPara;

Escribir
"Ingredientes seleccionados: ", seleccionados;
Limpiar
Pantalla;
FinSubProceso

SubProceso
SeleccionarEnsaladasYAderezos(tipoComida
Por
Referencia, ensalada
Por
Referencia, aderezos
Por
Referencia)
Definir
respuesta, ingrediente
Como
Cadena;
Definir
i
Como
Entero;
Definir
ingredientesEnsalada
Como
Caracter;
Definir
ingredientesAderezos
Como
Caracter;
Dimension
ingredientesEnsalada[3];
Dimension
ingredientesAderezos[6];

ensalada < - "";
aderezos < - "";

ingredientesEnsalada[0] < - "Lechuga";
ingredientesEnsalada[1] < - "Tomate";
ingredientesEnsalada[2] < - "Cebolla";

ingredientesAderezos[0] < - "Mayonesa";
ingredientesAderezos[1] < - "Mostaza";
ingredientesAderezos[2] < - "Ketchup";
ingredientesAderezos[3] < - "Salsa picante";
ingredientesAderezos[4] < - "Salsa BBQ";
ingredientesAderezos[5] < - "Salsa tartara";

Si
tipoComida = 1
O
tipoComida = 2
Entonces

Para
i < - 0
Hasta
2
Hacer
Escribir
"===============================";
Escribir
" ingredientes para su ensalada";
Escribir
"===============================";
ingrediente < - ingredientesEnsalada[i];
Escribir
"�Desea ", ingrediente, "? (S/N):";
Leer
respuesta;
Limpiar
Pantalla;
Si
Mayusculas(respuesta) = "S"
Entonces
ensalada < - Concatenar(ensalada, Concatenar(ingrediente, ", "));
FinSi;
FinPara;

Para
i < - 0
Hasta
5
Hacer
Escribir
"===============================";
Escribir
"     Seleccione aderezos:";
Escribir
"===============================";
ingrediente < - ingredientesAderezos[i];
Escribir
"�Desea ", ingrediente, "? (S/N):";
Leer
respuesta;
Limpiar
Pantalla;
Si
Mayusculas(respuesta) = "S"
Entonces
aderezos < - Concatenar(aderezos, Concatenar(ingrediente, ", "));
FinSi;
FinPara;
FinSi;

Escribir
"Ingredientes de ensalada seleccionados: ", ensalada;
Escribir
"Aderezos seleccionados: ", aderezos;
Limpiar
Pantalla;
FinSubProceso

SubProceso
SeleccionarAcompanamiento(precioAcom
Por
Referencia, acompanamientoTexto
Por
Referencia)
Definir
opcion
Como
Entero;
Definir
validoAcom
Como
Logico;

validoAcom < - Falso;

Repetir
Limpiar
Pantalla;
Escribir
"===============================";
Escribir
"     ----- ACOMPA�AMIENTO -----";
Escribir
"===============================";
Escribir
"1. Papas fritas       - $2.00";
Escribir
"2. Aros de cebolla    - $2.00";
Escribir
"3. Empanada           - $1.50";
Escribir
"4. Nuggets de pollo   - $2.50";
Escribir
"5. Ensalada rusa      - $1.75";
Escribir
"6. Ensalada cl�sica   - $1.50";
Escribir
"===============================";
Escribir
"Seleccione su acompa�amiento (1 a 6):";
Leer
opcion;

Si
opcion >= 1
Y
opcion <= 6
Entonces
validoAcom < - Verdadero;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
Esperar
1.5
Segundos;
FinSi;
Hasta
Que
validoAcom = Verdadero;

Segun
opcion
Hacer
1:
acompanamientoTexto < - "Papas fritas";
precioAcom < - 2.00;
2:
acompanamientoTexto < - "Aros de cebolla";
precioAcom < - 2.00;
3:
acompanamientoTexto < - "Empanada";
precioAcom < - 1.50;
4:
acompanamientoTexto < - "Nuggets de pollo";
precioAcom < - 2.50;
5:
acompanamientoTexto < - "Ensalada rusa";
precioAcom < - 1.75;
6:
acompanamientoTexto < - "Ensalada cl�sica";
precioAcom < - 1.50;
FinSegun;

Limpiar
Pantalla;
Escribir
"Acompa�amiento seleccionado: ", acompanamientoTexto;
Escribir
"Precio total del acompa�amiento: $", precioAcom;
Limpiar
Pantalla;
FinSubProceso

SubProceso
SeleccionarBebida(nombreBebida
Por
Referencia, precioBebida
Por
Referencia)
Definir
opcionBebida
Como
Entero;
Definir
entradaBebida
Como
Cadena;
Definir
validoBebida
Como
Logico;

validoBebida < - Falso;

Repetir
Escribir
"===============================";
Escribir
"----- BEBIDAS DISPONIBLES -----";
Escribir
"===============================";
Escribir
"1. Coca-Cola        - $1.50";
Escribir
"2. Pepsi            - $1.50";
Escribir
"3. Fanta            - $1.50";
Escribir
"4. Cerveza          - $2.00";
Escribir
"5. Agua             - $1.00";
Escribir
"6. Jugos Frutales   - $1.75";
Escribir
"===============================";
Escribir
"Seleccione una bebida (1 a 6):";

Leer
entradaBebida;

Si
entradaBebida = "1"
O
entradaBebida = "2"
O
entradaBebida = "3"
O
entradaBebida = "4"
O
entradaBebida = "5"
o
entradaBebida = "6"
Entonces
opcionBebida < - ConvertirANumero(entradaBebida);
validoBebida < - Verdadero;
Sino
Escribir
"Opci�n inv�lida. Intente de nuevo.";
validoBebida < - Falso;
FinSi;

Si
validoBebida = Falso
Entonces
Esperar
1.5
Segundos;
Limpiar
Pantalla;
FinSi;

Hasta
Que
validoBebida = Verdadero;

Segun
opcionBebida
Hacer
1:
nombreBebida < - "Coca-Cola";
precioBebida < - 1.50;
2:
nombreBebida < - "Pepsi";
precioBebida < - 1.50;
3:
nombreBebida < - "Fanta";
precioBebida < - 1.50;
4:
nombreBebida < - "Cerveza";
precioBebida < - 2.00;
5:
nombreBebida < - "Agua";
precioBebida < - 1.00;
6:
nombreBebida < - "Jugos Frutales";
precioBebida < - 1.75;
FinSegun;

Limpiar
Pantalla;
FinSubProceso

SubProceso
TicketCombos(nombreCombo, nombreBebida, precioComida, precioBebida)
Definir
Total, pago, vuelto
Como
Real;
Definir
numeroTicket, minutosEspera
Como
Entero;
numeroTicket < - Aleatorio(100, 999);
minutosEspera < - Aleatorio(10, 25);
Total < - preciocomida + precioBebida;
Escribir
"Total a pagar: $", Total;
Escribir
"Ingrese la cantidad con la que pagar�: ";
Leer
pago;
vuelto < - pago - Total;
Si
pago < Total
Entonces
Escribir
"Monto insuficiente. Por favor, ingrese un valor v�lido.";
Repetir
Escribir
"Ingrese nuevamente la cantidad con la que pagar�: ";
Leer
pago;
Hasta
Que
pago >= Total
FinSi
Limpiar
Pantalla;
Escribir
"";
Escribir
"===============================";
Escribir
"        TICKET DE COMPRA       ";
Escribir
"===============================";
Escribir
" Combo  : ", nombreCombo;
Escribir
" Bebida : ", nombreBebida;
Escribir
"===============================";
Escribir
" Precio Combo  : $", precioComida;
Escribir
" Precio Bebida : $", precioBebida;
Escribir
"===============================";
Escribir
" TOTAL A PAGAR : $", total;
Escribir
" MONTO ENTREGADO: $", pago;
Escribir
" VUELTO         : $", vuelto;
Escribir
"===============================";
Escribir
"Su orden estar� lista en ", minutosEspera, " minutos.";
Escribir
"N�mero de ticket: #", numeroTicket;
Escribir
"===============================";
Esperar
2
Segundos;
Escribir
"";
Escribir
"Gracias por su compra. �Buen provecho!";
Esperar
1.5
Segundos;
FinSubProceso

SubProceso
TicketPizza(tipoMasa, tipoSalsa, precioSalsa, tipoQueso, precioQueso, seleccionados, acompanamientoTexto, precioAcom,
            precioBebida, nombreBebida)
Definir
total, pago, vuelto
Como
Real;
Definir
numeroTicket, minutosEspera
Como
Entero;
numeroTicket < - Aleatorio(100, 999);
minutosEspera < - Aleatorio(10, 25);
total < - precioSalsa + precioQueso + precioAcom + precioBebida;
Escribir
"Total a pagar: $", total;
Escribir
"Ingrese la cantidad con la que pagar�: ";
Leer
pago;
vuelto < - pago - total;
Si
pago < total
Entonces
Escribir
"Monto insuficiente. Por favor, ingrese un valor v�lido.";
Repetir
Escribir
"Ingrese nuevamente la cantidad con la que pagar�: ";
Leer
pago;
Hasta
Que
pago >= total
FinSi
Limpiar
Pantalla;
Escribir
"===============================";
Escribir
"         TICKET DE PIZZA       ";
Escribir
"===============================";
Escribir
"Masa: ", tipoMasa;
Escribir
"Salsa: ", tipoSalsa, " ($", precioSalsa, ")";
Escribir
"Queso: ", tipoQueso, " ($", precioQueso, ")";
Escribir
"Ingredientes adicionales:";
Escribir
"", seleccionados;
Escribir
"Acompa�amiento: ", acompanamientoTexto, " ($", precioAcom, ")";
Escribir
"Bebida: ", nombreBebida, " ($", precioBebida, ")";
Escribir
"-------------------------------";
Escribir
"TOTAL A PAGAR: $", total;
Escribir
"MONTO PAGADO: $", pago;
Escribir
"VUELTO: $", vuelto;
Escribir
"===============================";
Escribir
"Su orden estar� lista en ", minutosEspera, " minutos.";
Escribir
"N�mero de ticket: #", numeroTicket;
Esperar
2
Segundos;
Escribir
"";
Escribir
"Gracias por su compra. �Buen provecho!";

FinSubProceso

SubProceso
TicketHamburguesaYSandwich(tipoComida, tipoPan, tipoCarne, ensalada, aderezos, acompanamientoTexto, Precio, precioAcom,
                           precioBebida, nombreBebida)
Definir
nombreComida
Como
Cadena;
Definir
TotalPer, pago, vuelto
Como
Real;
Definir
numeroTicket, minutosEspera
Como
Entero;
numeroTicket < - Aleatorio(100, 999);
minutosEspera < - Aleatorio(10, 25);
TotalPer < - Precio + precioAcom + precioBebida;
Escribir
"Total a pagar: $", TotalPer;
Escribir
"Ingrese la cantidad con la que pagar�: ";
Leer
pago;
vuelto < - pago - TotalPer;
Si
pago < TotalPer
Entonces
Escribir
"Monto insuficiente. Por favor, ingrese un valor v�lido.";
Repetir
Escribir
"Ingrese nuevamente la cantidad con la que pagar�: ";
Leer
pago;
Hasta
Que
pago >= TotalPer
FinSi
Limpiar
Pantalla;
Segun
tipoComida
Hacer
1: nombreComida < - "Hamburguesa Personalizada";
2: nombreComida < - "S�ndwich Personalizado";
FinSegun;

Limpiar
Pantalla;
Escribir
"===============================";
Escribir
"        TICKET DE COMPRA       ";
Escribir
"===============================";
Escribir
"Producto: ", nombreComida;

Si
tipoComida = 1
O
tipoComida = 2
Entonces
Escribir
"Pan: ", tipoPan;
Escribir
"Carne: ", tipoCarne;
Escribir
"Ensalada: ", ensalada;
Escribir
"Aderezos: ", aderezos;
FinSi;
Escribir
"acompa�amiento: ", acompanamientoTexto;
Escribir
"Bebida: ", nombreBebida;
Escribir
"Precio Hamburguesa: $", Precio;
Escribir
"Precio Acompa�amiento: $", precioAcom;
Escribir
"Precio Bebida: $", precioBebida;
Escribir
"-------------------------------";
Escribir
"Total a pagar: $", TotalPer;
Escribir
"MONTO PAGADO: $", pago;
Escribir
"VUELTO: $", vuelto;
Escribir
"===============================";
Escribir
"Su orden estar� lista en ", minutosEspera, " minutos.";
Escribir
"N�mero de ticket: #", numeroTicket;
Escribir
"Gracias por su compra!";
Escribir
"===============================";
Esperar
2
Segundos;
Escribir
"";
Escribir
"Gracias por su compra. �Buen provecho!";

FinSubProceso