using System;
using System.Collections.Generic;
using System.Runtime.Serialization;
using System.Text;

namespace Zadanie1
{
    [Serializable]
    public class Member : ISerializable
    {
        public string name { get; set; }
        public string surname { get; set; }

        public Member(string name, string surname)
        {
            this.name = name;
            this.surname = surname;
        }

        public Member(SerializationInfo info, StreamingContext context)
        {
            name = (string)info.GetValue("name", typeof(string));
            surname = (string)info.GetValue("surname", typeof(string));
        }

        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.AddValue("name", name, typeof(string));
            info.AddValue("surname", surname, typeof(string));
        }
    }
}
