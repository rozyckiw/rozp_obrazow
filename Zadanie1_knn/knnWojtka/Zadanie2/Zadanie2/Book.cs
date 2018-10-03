using System;
using System.Runtime.Serialization;

namespace Zadanie1
{
    [Serializable]
    public class Book: ISerializable
    {
        public string title { get; set; }
        public string surname { get; set; }

        public Book() { }

        public Book(string title, string surname)
        {
            this.title = title;
            this.surname = surname;
        }

        public Book(SerializationInfo info, StreamingContext context)
        {
            title = (string)info.GetValue("title", typeof(string));
            surname = (string)info.GetValue("surname", typeof(string));
        }

        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.AddValue("title", title, typeof(string));
            info.AddValue("surname", surname, typeof(string));
        }
    }
}
