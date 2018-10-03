using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Xml.Serialization;
using System.Collections.ObjectModel;
using Newtonsoft.Json;

namespace Zadanie1
{
    public class JsonSerialization
    {
        public DataContext Dserialization(string path)
        {
            string dser = File.ReadAllText(path);
            DataContext database = JsonConvert.DeserializeObject<DataContext>(dser, new JsonSerializerSettings { PreserveReferencesHandling = PreserveReferencesHandling.Objects });
            return database;
        }

        public void Serialization(string path, DataContext data)
        {
            string ser = JsonConvert.SerializeObject(data, Formatting.Indented, new JsonSerializerSettings { PreserveReferencesHandling = PreserveReferencesHandling.Objects });

            File.WriteAllText(path, ser);
        }
    }
}
