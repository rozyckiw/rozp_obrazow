using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;

namespace Zadanie1
{
    class DataService
    {
        private DataRepository repository;

        public DataService(DataRepository repository)
        {
            this.repository = repository;
        }

        //Wyswietlanie kolekcji:
        public void WriteActions(IEnumerable<Action> listAction)
        {
            foreach (Action item in listAction)
            {
                Console.WriteLine(item);
            }
        }

        public void WriteBooks(IEnumerable<Book> listBook)
        {
            foreach (Book item in listBook)
            {
                Console.WriteLine(item);
            }
        }

        public void WriteBookDetails(IEnumerable<BookDetails> listBookDetails)
        {
            foreach (BookDetails item in listBookDetails)
            {
                Console.WriteLine(item);
            }
        }

        public void WriteMember(IEnumerable<Member> listMember)
        {
            foreach (Member item in listMember)
            {
                Console.WriteLine(item);
            }
        }

        //Dodawanie zdarzen i wykazow:
        public Action AddAction(Member member, BookDetails bookDetails, string action)
        {
            Action actions = new Action(member, bookDetails);
            return actions;
        }

        public BookDetails AddBookDetails(string description, int availableAmount, int generalAmount, int tax, int nettoPrice, Book book)
        {
            BookDetails bookDet = new BookDetails(description, book);
            return bookDet;
        }

        //Wyswietlanie powiązanych kolekcji:
        public void WriteActionForMember(IEnumerable<Action> listAction, IEnumerable<Member> listMember)
        {
            foreach(Member item in listMember)
            {
                Console.WriteLine(item);
                foreach(Action item1 in listAction)
                {
                    if (item.Equals(item1.who))
                    {
                        Console.WriteLine(item1.bookInfo.bookDet.title + ' ' + item1.bookInfo);     //Do ulepszenia
                    }
                }
            }
        }

        public IEnumerable<Book> GetAllBookFromDictionary()
        {
            return repository.GetAllBooks();
        }

        //Filtrowanie
        public IEnumerable<Action> ActionByMember(Member member)
        {
            List<Action> actions = new List<Action>();
            
            foreach(Action item in repository.GetAllAction())
            {
                if (item.who.Equals(member))
                {
                    actions.Add(item);
                }
            }

            return actions;
        }

        public IEnumerable<Action> ActionByDate(DateTime from, DateTime to)
        {
            List<Action> actions = new List<Action>();

            foreach (Action item in repository.GetAllAction())
            {
                if (item.actionDate>=from && item.actionDate<=to)
                {
                    actions.Add(item);
                }
            }

            return actions;
        }
    }
}
