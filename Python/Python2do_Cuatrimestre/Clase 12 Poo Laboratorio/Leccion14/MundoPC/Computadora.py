# CLASE 12 POO Laboratorio

# Importamos las clases necesarias para que la clase Computadora pueda usarlas (composición).
# Estas clases deben estar definidas en archivos separados (Teclado.py, Raton.py, Monitor.py).
from Teclado import *
from Raton import *
from Monitor import *


# Creamos una clase independiente: COMPUTADORA (video 7 Py)
class Computadora:
    # --- Atributos de Clase ---
    # Contador de clase: Se utiliza para asignar un ID único a cada instancia de Computadora que se crea.
    contadorComputadora = 0

    # --- Constructor (Método de Inicialización) ---
    # Recibe el nombre de la PC y los objetos que la componen: monitor, teclado y ratón.
    def __init__(self, nombre, monitor, teclado, raton):
        # 1. Incrementamos el contador de clase para obtener el siguiente ID.
        Computadora.contadorComputadora += 1

        # 2. Asignamos el ID único a la nueva instancia.
        self.idComputadora = Computadora.contadorComputadora

        # 3. Asignamos los parámetros de entrada a los atributos de instancia.
        # Almacena la cadena con el nombre de la computadora.
        self._nombre = nombre
        # Almacena un objeto de tipo Monitor (Composición: la PC "tiene un" Monitor).
        self._monitor = monitor
        # Almacena un objeto de tipo Teclado (Composición: la PC "tiene un" Teclado).
        self._teclado = teclado
        # Almacena un objeto de tipo Ratón (Composición: la PC "tiene un" Ratón).
        self._raton = raton

    # --- Propiedades (Getters y Setters) ---
    # Los 'getters' permiten acceder a los atributos encapsulados (los que empiezan con _).
    # Los 'setters' permiten modificar estos atributos de forma controlada.

    @property  # Getter para obtener el nombre
    def nombre(self):
        return self._nombre

    @nombre.setter  # Setter para modificar el nombre
    def nombre(self, nombre):
        self._nombre = nombre

    @property  # Getter para obtener el objeto Monitor
    def monitor(self):
        return self._monitor

    @monitor.setter  # Setter para modificar el objeto Monitor
    def monitor(self, monitor):
        self._monitor = monitor

    @property  # Getter para obtener el objeto Teclado
    def teclado(self):
        return self._teclado

    @teclado.setter  # Setter para modificar el objeto Teclado
    def teclado(self, teclado):
        self._teclado = teclado

    @property  # Getter para obtener el objeto Ratón
    def raton(self):
        return self._raton

    @raton.setter  # Setter para modificar el objeto Ratón
    def raton(self, raton):
        self._raton = raton

    # --- Método Especial de Representación (String) ---
    # Define cómo se ve la instancia de Computadora cuando se imprime (e.g., print(pc1)).
    def __str__(self):
        # Utilizamos una f-string con triple comillas para un formato multilínea y legible.
        # Nota: Cuando se llama a {self._monitor}, Python automáticamente llama
        # al método __str__ del objeto Monitor, y lo mismo para Teclado y Ratón.
        return f"""
                Nombre: {self._nombre}: ID {self.idComputadora}
                Monitor: {self._monitor}
                Teclado: {self._teclado}
                Raton: {self._raton}
        """


# --- Bloque de Pruebas (Solo se ejecuta si este archivo es el principal) ---
if (__name__ == "__main__"):
    # --- Objeto 1: Creación de componentes y de la PC ---
    raton1 = Raton("Logitech", "Bluetoon")
    teclado1 = Teclado("Redragon", "USB")
    monitor1 = Monitor("samsung", 28)

    # Creamos la primera instancia de Computadora.
    # Los argumentos que pasamos son los objetos *reales* de los componentes.
    pc1 = Computadora("PC gamer", monitor1, teclado1, raton1)
    print(pc1)  # Llama al método __str__ para imprimir la información de pc1.

    # --- Objeto 2: Creación de componentes y de la PC ---
    raton2 = Raton("Genérico", "USB")
    teclado2 = Teclado("Genérico", "USB")
    monitor2 = Monitor("Genérico", 24)

    # Creamos la segunda instancia de Computadora. El contadorComputadora se incrementa a 2.
    pc2 = Computadora("PC Trabajo", monitor2, teclado2, raton2)
    print(pc2)  # Llama al método __str__ para imprimir la información de pc2.