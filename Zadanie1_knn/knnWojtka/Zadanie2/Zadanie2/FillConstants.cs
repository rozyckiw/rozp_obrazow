using System;
using System.Collections.Generic;
using System.Text;

namespace Zadanie1
{
    public class FillConstants : IDataFiller
    {
        public void Fill(DataContext context, long howMany)
        {
            //moi przyjaciele
            Member member_1 = new Member("Pawel", "Tomaszewski");
            Member member_2 = new Member("Michal", "Cieplak");
            Member member_3 = new Member("Lukasz", "Nadarzyński");
            Member member_4 = new Member("Wojchiech", "Rozycki");
            Member member_5 = new Member("Michal", "Pelenski");
            Member member_6 = new Member("Aneta", "Wisniewska");
            Member member_7 = new Member("Janusz", "Tomaszewski");
            Member member_8 = new Member("Piotr", "Myslinski");
            Member member_9 = new Member("Damian", "Rudnicki");
            Member member_10 = new Member("Lukasz", "Marzec");

            context.members.Add(member_1);
            context.members.Add(member_2);
            context.members.Add(member_3);
            context.members.Add(member_4);
            context.members.Add(member_5);
            context.members.Add(member_6);
            context.members.Add(member_7);
            context.members.Add(member_8);
            context.members.Add(member_9);
            context.members.Add(member_10);

            //Ksiazki
            Book book_1 = new Book("Krzyzacy", "Sienkiewicz");
            Book book_2 = new Book("Ogniem i mieczem", "Sienkiewicz");
            Book book_3 = new Book("W pustyni i w puszczy", "Sienkiewicz");
            Book book_4 = new Book("Kamienie na szaniec", "Kaminski");
            Book book_5 = new Book("Pan Tadeusz", "Mickiewicz");
            Book book_6 = new Book("Dziady cz.2", "Mickiewicz");
            Book book_7 = new Book("Kamizelka", "Prus");
            Book book_8 = new Book("Zemsta", "Fredro");
            Book book_9 = new Book("Balladyna", "Slowacki");
            Book book_10 = new Book("Wesele", "Wyspianski");

            context.books.Add(1, book_1);
            context.books.Add(2, book_2);
            context.books.Add(3, book_3);
            context.books.Add(4, book_4);
            context.books.Add(5, book_5);
            context.books.Add(6, book_6);
            context.books.Add(7, book_7);
            context.books.Add(8, book_8);
            context.books.Add(9, book_9);
            context.books.Add(10, book_10);

            //Ksiazka plus
            BookDetails bookDetails_1 = new BookDetails("Powieść historyczna", book_1);
            BookDetails bookDetails_2 = new BookDetails("Powiesc historyczna", book_2);
            BookDetails bookDetails_3 = new BookDetails("Powiesc przygodowa", book_3);
            BookDetails bookDetails_4 = new BookDetails("Literatura faktu", book_4);
            BookDetails bookDetails_5 = new BookDetails("Poemat", book_5);
            BookDetails bookDetails_6 = new BookDetails("Dramat", book_6);
            BookDetails bookDetails_7 = new BookDetails("Nowela", book_7);
            BookDetails bookDetails_8 = new BookDetails("Komedia", book_8);
            BookDetails bookDetails_9 = new BookDetails("Tragedia", book_9);
            BookDetails bookDetails_10 = new BookDetails("Dramat", book_10);

            context.booksDetails.Add(bookDetails_1);
            context.booksDetails.Add(bookDetails_2);
            context.booksDetails.Add(bookDetails_3);
            context.booksDetails.Add(bookDetails_4);
            context.booksDetails.Add(bookDetails_5);
            context.booksDetails.Add(bookDetails_6);
            context.booksDetails.Add(bookDetails_7);
            context.booksDetails.Add(bookDetails_8);
            context.booksDetails.Add(bookDetails_9);
            context.booksDetails.Add(bookDetails_10);

            //Zdarzenie
            context.actions.Add(new Action(member_1, bookDetails_1));
            context.actions.Add(new Action(member_8, bookDetails_2));
            context.actions.Add(new Action(member_3, bookDetails_8));
            context.actions.Add(new Action(member_7, bookDetails_4));
            context.actions.Add(new Action(member_2, bookDetails_3));
            context.actions.Add(new Action(member_6, bookDetails_1));
            context.actions.Add(new Action(member_9, bookDetails_7));
            context.actions.Add(new Action(member_8, bookDetails_8));
            context.actions.Add(new Action(member_9, bookDetails_9));
            context.actions.Add(new Action(member_10, bookDetails_2));
            context.actions.Add(new Action(member_1, bookDetails_10));
            context.actions.Add(new Action(member_4, bookDetails_2));
            context.actions.Add(new Action(member_9, bookDetails_3));
            context.actions.Add(new Action(member_4, bookDetails_2));
            context.actions.Add(new Action(member_1, bookDetails_9));
            context.actions.Add(new Action(member_8, bookDetails_10));
            context.actions.Add(new Action(member_7, bookDetails_7));
            context.actions.Add(new Action(member_8, bookDetails_3));
            context.actions.Add(new Action(member_3, bookDetails_9));
            context.actions.Add(new Action(member_1, bookDetails_3));
        }
    }
}
