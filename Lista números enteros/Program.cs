




// Preguntar si quiere añadir otro número y guardar en variable (Response)
// Mostrar por consola lista de números de menor a mayor
// Dejar elegir al usuario cómo ordenar (ASC/DESC)




bool confirmed = false;
string Key;

// Crear lista de numeros y llamarla NumberList (vacia)
List<string> NumberList = new List<string>();

// Crear variable Response
string Response = Console.ReadLine();

// Crear un bucle do while con la condición Response != NO
do
{
    // Preguntar al usuario que número quiere añadir y guardar en variable (NumberList)
    Console.WriteLine("Introduzca un número entero:");
    int.Parse(Console.ReadLine());

    string NúmeroEntero = Console.ReadLine();
    NumberList.Add(NúmeroEntero);

    
    

  


} while (Response == ConsoleKey.N);



  Console.WriteLine("Quieres añadir otro número? [Y/N{]");
  Key = Console.ReadLine();



