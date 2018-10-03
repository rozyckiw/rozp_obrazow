using System;
using System.Collections.Generic;
using System.Text;

namespace Zadanie1
{
    public class FillRandom : IDataFiller
    {
        public void Fill(DataContext context, long howMany)
        {
            Random rand = new Random();

            List<string> names = new List<string>();
            List<string> surNames = new List<string>();
            List<string> titles = new List<string>();
            List<string> descriptions = new List<string>();

            //Dodawanie Imion
            names.Add("Pawel");
            names.Add("Damian");
            names.Add("Wojciech");
            names.Add("Michal");
            names.Add("Piotr");
            names.Add("Aneta");
            names.Add("Janusz");
            names.Add("Beata");
            names.Add("Grzegorz");
            names.Add("Zofia");

            //Dodawanie Nazwisk
            surNames.Add("Tomaszewski");
            surNames.Add("Rudnicki");
            surNames.Add("Walczak");
            surNames.Add("Mickiewicz");
            surNames.Add("Sienkiewicz");
            surNames.Add("Prus");
            surNames.Add("Pelenski");
            surNames.Add("Wisniewska");
            surNames.Add("Smolarek");
            surNames.Add("Lewandowski");

            //Dodawanie tytulow
            titles.Add("Ogniem i mieczem");
            titles.Add("W pustyni i w puszczy");
            titles.Add("Mis");
            titles.Add("Brud");
            titles.Add("Lalka");
            titles.Add("Pan Tadeusz");
            titles.Add("Kamizelka");
            titles.Add("Sweter");
            titles.Add("Programowanie");
            titles.Add("Zwiadowcy");

            //Dodawanie opisow
            descriptions.Add("Powiesc historyczna");
            descriptions.Add("Powiesc przygodowa");
            descriptions.Add("Dramat");
            descriptions.Add("Tragedia");
            descriptions.Add("Bajka");
            descriptions.Add("Fraszka");
            descriptions.Add("Komedia");
            descriptions.Add("Poemat");
            descriptions.Add("Ksiazka naukowa");
            descriptions.Add("Wiersz");

            //Uzupełnianie kolekcji
            for (int i = 0; i < howMany; i++)
            {
                Member member = new Member(names[rand.Next(names.Count)], surNames[rand.Next(surNames.Count)]);
                Book book = new Book(titles[rand.Next(titles.Count)], surNames[rand.Next(surNames.Count)]);
                BookDetails bookDetails = new BookDetails(descriptions[rand.Next(descriptions.Count)], book);
                context.members.Add(member);
                context.books.Add(i, book);
                context.booksDetails.Add(bookDetails);
                context.actions.Add(new Action(member, bookDetails));
            }
        }
    }
}
