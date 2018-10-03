using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;

namespace Zadanie1
{
    public class OwnSerialization
    {
        public DataContext Dserialization(string path)
        {
            FileStream stream = new FileStream(path, FileMode.Open);
            IFormatter formatter = new BinaryFormatter();
            DataContext database = (DataContext)formatter.Deserialize(stream);
            return database;
        }

        public void Serialization(string path, DataContext database)
        {
            IFormatter formatter = new BinaryFormatter();
            FileStream stream = new FileStream(path, FileMode.Create);
            formatter.Serialize(stream, database);
            stream.Close();
        }
    }
}
