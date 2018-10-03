using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Zadanie1;


namespace Zadanie2.Cons
{
    class Program
    { 

        static void Main(string[] args)
        {

            DataContext dataContext         = new DataContext();
            FillRandom fill = new FillRandom();
            DataRepository dataRepository   = new DataRepository(fill, dataContext, true);
            bool mainMenu = true;
            JsonSerialization jserializacja = new JsonSerialization();
            OwnSerialization oserializacja = new OwnSerialization();

            //menu:
            char choice = '0', choice2 = '0';
            do
            {
                Console.Clear();
                Console.WriteLine("Witaj!");
                Console.WriteLine("\n__________________________________________________________________");
                Console.WriteLine();
                Console.WriteLine("1: Zapisywanie");
                Console.WriteLine("2: Odczytywanie");
                Console.WriteLine("3: Koniec programu");
                Console.WriteLine("__________________________________________________________________ \n");
                Console.Write("Wybierz co chcesz zrobić dalej: ");
                if (mainMenu)
                    choice = Console.ReadKey().KeyChar; //wybór użytkownika

                if (choice == '1' || choice == '2')
                {
                    Console.Clear();
                    Console.WriteLine("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n");
                    Console.WriteLine("1: Serializacja własna");
                    Console.WriteLine("2: Serializacja korzystająca z json \n");
                    Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n");
                    Console.Write("Wybierz co chcesz zrobić dalej: ");
                    choice2 = Console.ReadKey().KeyChar; //wybór użytkownika
                    mainMenu = false;

                    if (choice == '1')
                    {
                        if (choice2 == '1')
                        {
                            oserializacja.Serialization("own.bin", dataContext);
                        }

                        if (choice2 == '2')
                        {
                            jserializacja.Serialization("json.tomaszewski&rozycki", dataContext);
                        }
                            
                    }
  
                    else if (choice == '2' && choice2 == '1')
                    {
                        oserializacja.Dserialization("own.bin");
                    }

                    else if (choice == '2' && choice2 == '2')
                    {
                        dataContext = jserializacja.Dserialization("json.tomaszewski&rozycki");
                    }

                    mainMenu = true;
                }
            }
            while (choice != '3');
        }
    }
}

