using System;
using Zadanie1;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Collections.Generic;
using System.Linq;


namespace Zadanie1.Tests
{
    [TestClass]
    public class Zadanie1
    {
        [TestMethod]
        public void addBookTest()
        {
            Book book = new Book("testTytul", "testNazwisko");
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.books.Count;
            library.AddBook(book, 0);
            
            Assert.AreEqual(num+1, database.books.Count, "Ksiazke dodano nieprawidlowo");
        }

        [TestMethod]
        public void getBookTest()
        {
            Book book = new Book("testTytul", "testNazwisko");
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            library.AddBook(book, 0);
            bool val = library.GetBook(0).Equals(book);
            Assert.AreEqual(true, val, "Nie znaleziono pozycji");
        }

        [TestMethod]
        public void updateBookTest()
        {
            string title = "testTytul";
            string newTitle = "nowyTestTytul";
            Book book = new Book(title, "testNazwisko");
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            library.AddBook(book, 0);
            Book newBook = new Book(newTitle, "nowyTestNazwisko");
            library.UpdateBook(newBook, 0);
            bool val = library.GetBook(0).Equals(newBook);
            Assert.AreEqual(true, val, "Nie zaktualizowano pozycji");
        }

        [TestMethod]
        public void deleteBookTest()
        {
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.books.Count;
            library.DeleteBook(num);
            Assert.AreEqual(num-1, database.books.Count, "Ksiazke usunieto nieprawidlowo");
        }

        [TestMethod]
        public void IEnumerableTest()
        {
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            IEnumerable<Book> books = library.GetAllBooks();
            IEnumerable<BookDetails> details = library.GetAllBookDetails();
            IEnumerable<Action> actions = library.GetAllAction();
            IEnumerable<Member> members = library.GetAllMember();

            Assert.AreEqual(books.Count(), database.books.Count, "Lista ksiazek zaladowana nieprawidlowo");
            Assert.AreEqual(details.Count(), database.booksDetails.Count, "Lista detali zaladowana nieprawidlowo");
            Assert.AreEqual(actions.Count(), database.actions.Count, "Lista akcji zaladowana nieprawidlowo");
            Assert.AreEqual(members.Count(), database.members.Count, "Lista czlonkow zaladowana nieprawidlowo");
        }

        [TestMethod]
        public void addBookDetailsTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda", book);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.books.Count+1;
            library.AddBook(book, num);
            library.AddBookDetails(bookDet);
            BookDetails checkedDetails = database.booksDetails[num-1];
            Assert.AreEqual(checkedDetails, bookDet, "Informacje ksiazki dodane nieprawidlowo");
        }

        [TestMethod]
        public void getBookDetailsTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda",  book);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.books.Count + 1;
            library.AddBook(book, num);
            library.AddBookDetails(bookDet);
            library.GetBookDetails(num-1);
            bool val = library.GetBookDetails(num-1).Equals(bookDet);
            Assert.AreEqual(true, val, "Informacje ksiazki dodane nieprawidlowo");
        }

        [TestMethod]
        public void updateBookDetailsTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda", book);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            library.AddBook(book, 0);
            library.AddBookDetails(bookDet);
            string newTitle = "newTestTytul";
            Book book2 = new Book(newTitle, "testNazwisko");
            BookDetails bookDet2 = new BookDetails("Przygoda", book2);
            library.UpdateBookDetails(bookDet2, 0);
            bool val = library.GetBookDetails(0).Equals(bookDet2);
            Assert.AreEqual(true, val, "Informacje ksiazki zaktualizowane nieprawidlowo");
        }

        [TestMethod]
        public void deleteBookDetailsTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda", book);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.books.Count + 1;
            library.AddBook(book, num);
            library.AddBookDetails(bookDet);
            library.DeleteBookDetails(bookDet);
            Assert.AreEqual(num-1, database.booksDetails.Count, "Informacje ksiazki usunieto nieprawidlowo");
        }

        [TestMethod]
        public void addActionTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda", book);
            Member member = new Member("testImie", "testNazwisko");
            Action action = new Action(member, bookDet);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.actions.Count;
            library.AddAction(action);
            Assert.AreEqual(num+1, database.actions.Count, "Akcja dodana nieprawidlowo");
        }

        [TestMethod]
        public void getActionTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda", book);
            Member member = new Member("testImie", "testNazwisko");
            Action action = new Action(member, bookDet);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.actions.Count;
            library.AddAction(action);
            bool val = library.GetAction(num).Equals(action);
            Assert.AreEqual(true, val, "Nie znaleziono pozycji");
        }

        [TestMethod]
        public void updateActionTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda", book);
            Member member = new Member("testImie", "testNazwisko");
            Action action = new Action(member, bookDet);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            library.AddAction(action);

            string title2 = "testTytul2";
            Book book2 = new Book(title2, "testNazwisko");
            BookDetails bookDet2 = new BookDetails("Przygoda", book2);
            Member member2 = new Member("testImie2", "testNazwisko2");
            Action action2 = new Action(member2, bookDet2);
            library.UpdateAction(action2, 0);
            bool val = library.GetAction(0).Equals(action2);
            Assert.AreEqual(true, val, "Nie znaleziono pozycji");
        }

        [TestMethod]
        public void deleteActionTest()
        {
            string title = "testTytul";
            Book book = new Book(title, "testNazwisko");
            BookDetails bookDet = new BookDetails("Przygoda",  book);
            Member member = new Member("testImie", "testNazwisko");
            Action action = new Action(member, bookDet);
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.actions.Count;
            library.AddAction(action);
            library.DeleteAction(action);
            Assert.AreEqual(num, database.actions.Count, "Pozycja usunieta nieprawidlowo");
        }


        [TestMethod]
        public void addMemberTest()
        {
            Member member = new Member("testImie", "testNazwisko");
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.members.Count;
            library.AddMember(member);
            Assert.AreEqual(num+1, database.members.Count, "Członek dodany nieprawidlowo");
        }

        [TestMethod]
        public void getMemberTest()
        {
            Member member = new Member("testImie", "testNazwisko");
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            int num = database.members.Count;
            library.AddMember(member);
            bool val = library.GetMember(num).Equals(member);
            Assert.AreEqual(true, val, "Nie znaleziono pozycji członka");
        }

        [TestMethod]
        public void updateMemberTest()
        {
            Member member = new Member("testImie", "testNazwisko");
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            library.AddMember(member);

            Member member2 = new Member("testImie2", "testNazwisko2");
            library.UpdateMember(member2, 0);

            bool val = library.GetMember(0).Equals(member2);
            Assert.AreEqual(true, val, "Nie znaleziono pozycji nowego członka");
        }

        [TestMethod]
        public void deleteMemberTest()
        {
            Member member = new Member("testImie", "testNazwisko");
            DataContext database = new DataContext();
            FillConstants fill = new FillConstants();
            DataRepository library = new DataRepository(fill, database, true);
            library.AddMember(member);
            int num = database.members.Count;
            library.DeleteMember(member);
            Assert.AreEqual(num-1, database.members.Count, "Pozycja usunieta nieprawidlowo");
        }

        [TestMethod]
        public void fillConstantsTest()
        {

            FillConstants fillConst = new FillConstants();
            DataContext database = new DataContext();
            int expID = 10;

            fillConst.Fill(database, 1);

            Assert.AreEqual(expID, database.members.Count, "Czlonkowie dodani nieprawidlowo");
            Assert.AreEqual(expID, database.books.Count, "Ksiazki dodane nieprawidlowo");
            Assert.AreEqual(expID, database.booksDetails.Count, "Detale ksiazek dodane nieprawidlowo");
            Assert.AreEqual(expID * 2, database.actions.Count, "Akcje dodane nieprawidlowo");

        }

        [TestMethod]
        public void fillRandomTest()
        {

            FillRandom fillRandom = new FillRandom();
            DataContext database = new DataContext();
            long loops = 1000000;

            fillRandom.Fill(database, loops);

            Assert.AreEqual(loops, database.members.Count, "Czlonkowie dodani nieprawidlowo");
            Assert.AreEqual(loops, database.books.Count, "Ksiazki dodane nieprawidlowo");
            Assert.AreEqual(loops, database.booksDetails.Count, "Detale ksiazek dodane nieprawidlowo");
            Assert.AreEqual(loops, database.actions.Count, "Akcje dodane nieprawidlowo");

        }
    }
}
