
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); //Llamado al constructor o instancia u Objeto
        persona1.nombre = "Cecilia"; //El valor exadecimal normalmente comienza con 0x
        persona1.apellido = "Farias";
        persona1.obtenerInformacion();

        Persona persona2 = new Persona();
        System.out.println("persona2 ="+persona2);
        System.out.println("persona1 ="+persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giodanini";
        persona2.obtenerInformacion();
    }
}
