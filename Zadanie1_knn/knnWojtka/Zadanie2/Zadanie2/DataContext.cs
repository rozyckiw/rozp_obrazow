using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using System.Text;

namespace Zadanie1
{
    [Serializable]
    public class DataContext : ISerializable
    {
        public List<Member> members { get; set; }
        public Dictionary<int, Book> books { get; set; }
        public ObservableCollection<Action> actions { get; set; }
        public List<BookDetails> booksDetails { get; set; }

        public DataContext()
        {
            members = new List<Member>();
            booksDetails = new List<BookDetails>();
            books = new Dictionary<int, Book>();
            actions = new ObservableCollection<Action>();
            actions.CollectionChanged += Actions_CollectionChanged;
        }

        public DataContext(SerializationInfo info, StreamingContext context)
        {
            members = (List<Member>)info.GetValue("members", typeof(List<Member>));
            books = (Dictionary<int, Book>)info.GetValue("books", typeof(Dictionary<int, Book>));
            actions = (ObservableCollection<Action>)info.GetValue("actions", typeof(ObservableCollection<Action>));
            booksDetails = (List<BookDetails>)info.GetValue("bookDetails", typeof(List<BookDetails>));
        }

        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.AddValue("members", members, typeof(List<Member>));
            info.AddValue("books", books, typeof(Dictionary<int, Book>));
            info.AddValue("actions", actions, typeof(ObservableCollection<Action>));
            info.AddValue("bookDetails", booksDetails, typeof(List<BookDetails>));
        }

        private void Actions_CollectionChanged(object sender, System.Collections.Specialized.NotifyCollectionChangedEventArgs e)
        {
            if(e.Action == System.Collections.Specialized.NotifyCollectionChangedAction.Add)
            {
                Console.WriteLine("Dodano element");
            }

            if (e.Action == System.Collections.Specialized.NotifyCollectionChangedAction.Remove)
            {
                Console.WriteLine("Usunieto element element");
            }
        }
    }
}
