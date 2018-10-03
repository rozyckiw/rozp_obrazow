using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;

namespace Zadanie1
{
    public class DataRepository
    {
        private DataContext database;

        public DataRepository(IDataFiller filler, DataContext database1, bool fill)
        {
            this.database = database1;

            if(fill==true)
            filler.Fill(database, 10);
        }

        //public DataRepository(DataContext database1)
        //{
        //    this.database = database1;
        //}

        //-----------------------------------------Books----------------------------------------------
        public void AddBook(Book book, int key)
        {
            database.books.Add(key, book);
        }

        public Book GetBook(int key)
        {
            return database.books[key];
        }

        public IEnumerable<Book> GetAllBooks()
        {
            return database.books.Values.ToList();
        }

        public void UpdateBook(Book book, int key)
        {
            database.books[key] = book;
        }

        public void DeleteBook(int key)
        {
            database.books.Remove(key);
        }

        //-----------------------------------------BookDetails----------------------------------------------
        public void AddBookDetails(BookDetails bookDetails)
        {
            database.booksDetails.Add(bookDetails);
        }

        public BookDetails GetBookDetails(int key)
        {
            return database.booksDetails[key];
        }

        public IEnumerable<BookDetails> GetAllBookDetails()
        {
            return database.booksDetails;
        }

        public void UpdateBookDetails(BookDetails bookDetails, int key)
        {
            database.booksDetails[key] = bookDetails;
        }

        public void DeleteBookDetails(BookDetails bookDetails)
        {
            database.booksDetails.Remove(bookDetails);
        }

        //-----------------------------------------Action----------------------------------------------
        public void AddAction(Action action)
        {
            database.actions.Add(action);
        }

        public Action GetAction(int key)
        {
            return database.actions[key];
        }

        public IEnumerable<Action> GetAllAction()
        {
            return database.actions;
        }

        public void UpdateAction(Action action, int key)
        {
            database.actions[key] = action;
        }

        public void DeleteAction(Action action)
        {
            database.actions.Remove(action);  
        }

        //-----------------------------------------Member----------------------------------------------
        public void AddMember(Member member)
        {
            database.members.Add(member);
        }

        public Member GetMember(int key)
        {
            return database.members[key];
        }

        public IEnumerable<Member> GetAllMember()
        {
            return database.members;
        }

        public void UpdateMember(Member member, int key)
        {
            database.members[key] = member;
        }

        public void DeleteMember(Member member)
        {
            database.members.Remove(member);
        }
    }
}