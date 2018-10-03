using System;
using System.Collections.Generic;
using System.Runtime.Serialization;
using System.Text;
using System.Xml.Serialization;

namespace Zadanie1
{
    [Serializable]
    public class Action : ISerializable
    {
        public Member who { get;  set; }
        public BookDetails bookInfo { get; set; }
        public DateTime actionDate { get; set; }
        public DateTime actionDateLimit { get; set; }

        public Action() { }

        public Action(Member who, BookDetails bookInfo)
        {
            this.who = who;
            this.bookInfo = bookInfo;
            this.actionDate = DateTime.Now;
            this.actionDateLimit = actionDate.AddMonths(1);
        }

        public Action(SerializationInfo info, StreamingContext context)
        {
            who = (Member)info.GetValue("who", typeof(Member));
            bookInfo = (BookDetails)info.GetValue("bookInfo", typeof(BookDetails));
            actionDate = (DateTime)info.GetValue("actionDate", typeof(DateTime));
            actionDateLimit = (DateTime)info.GetValue("actionDateLimit", typeof(DateTime));
        }

        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.AddValue("who", who, typeof(Member));
            info.AddValue("bookInfo", bookInfo, typeof(BookDetails));
            info.AddValue("actionDate", actionDate, typeof(DateTime));
            info.AddValue("actionDateLimit", actionDateLimit, typeof(DateTime));
        }
    }
}
