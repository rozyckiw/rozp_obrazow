using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Linq;

namespace Zadanie1.Tests
{
    [TestClass]
    public class Zadanie2
    {
        [TestMethod]
        public void Json()
        {
            DataContext dataContext = new DataContext();
            FillRandom fill = new FillRandom();
            DataRepository dataRepository = new DataRepository(fill, dataContext, true);
            JsonSerialization jserializacja = new JsonSerialization();
            jserializacja.Serialization("json.tomaszewski&rozycki", dataContext);

            DataContext dataContext1 = jserializacja.Dserialization("json.tomaszewski&rozycki");
            DataRepository dataRepository1 = new DataRepository(fill, dataContext1, false);

            Assert.IsTrue(dataRepository.GetAllMember().Count() == dataRepository1.GetAllMember().Count());
            Assert.IsTrue(dataRepository.GetAllBooks().Count() == dataRepository1.GetAllBooks().Count());
            Assert.IsTrue(dataRepository.GetAllAction().Count() == dataRepository1.GetAllAction().Count());
            Assert.IsTrue(dataRepository.GetAllBookDetails().Count() == dataRepository1.GetAllBookDetails().Count());
        }

        [TestMethod]
        public void Own()
        {
            DataContext dataContext = new DataContext();
            FillRandom fill = new FillRandom();
            DataRepository dataRepository = new DataRepository(fill, dataContext, true);
            OwnSerialization oserializacja = new OwnSerialization();
            oserializacja.Serialization("own.bin", dataContext);

            DataContext dataContext1 = oserializacja.Dserialization("own.bin");
            DataRepository dataRepository1 = new DataRepository(fill, dataContext1, false);

            Assert.IsTrue(dataRepository.GetAllMember().Count() == dataRepository1.GetAllMember().Count());
            Assert.IsTrue(dataRepository.GetAllBooks().Count() == dataRepository1.GetAllBooks().Count());
            Assert.IsTrue(dataRepository.GetAllAction().Count() == dataRepository1.GetAllAction().Count());
            Assert.IsTrue(dataRepository.GetAllBookDetails().Count() == dataRepository1.GetAllBookDetails().Count());
        }
    }
}
