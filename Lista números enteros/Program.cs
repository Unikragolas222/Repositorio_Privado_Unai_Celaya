




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


// Crear ListOrdNúmeros 
List<string> ListOrdnúmeros = new List<string>();




while (ListOrdNúmeros.Count != 0)
{
    // Crear variable NumMax e inicializar a -1
    int NumMax = -1;

    // Recorrer NumberList Contar de 0 a tamaño de ListOrdNúmeros y llamar "x"
    for (int x = 0; x < ListProdQuant.Count; x++)
    {
        // Si elemento "x" de ListOrdNúmeros > NumMax
        if (ListOrdnúmeros[x] > NumMax)
        {
            // NumMax = valor de elemento "x" de ListOrdNúmeros
            NumMax = ListOrdnúmeros[x];
        }
    }
}

// Imprimir por pantalla todos los Números de la lista ordenada
Console.WriteLine("La lista ordenada quedaría así:");
