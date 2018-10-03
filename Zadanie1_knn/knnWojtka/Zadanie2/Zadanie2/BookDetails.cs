using System;
using System.Collections.Generic;
using System.Runtime.Serialization;
using System.Text;

namespace Zadanie1
{
    [Serializable]
    public class BookDetails : ISerializable
    {
        public string description { get; set; } //przygodowa itd.
        public DateTime buyDate { get; set; }
        public Book bookDet { get; set; }

        public BookDetails() { }

        public BookDetails(string description, Book bookDet)
        {
            this.description = description;
            this.bookDet = bookDet;
            this.buyDate = DateTime.Now;
        }

        public BookDetails(SerializationInfo info, StreamingContext context)
        {
            description = (string)info.GetValue("description", typeof(string));
            buyDate = (DateTime)info.GetValue("buyDate", typeof(DateTime));
            bookDet = (Book)info.GetValue("bookDet", typeof(Book));
        }

        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.AddValue("description", description, typeof(string));
            info.AddValue("buyDate", buyDate, typeof(DateTime));
            info.AddValue("bookDet", bookDet, typeof(Book));
        }
    }
}
