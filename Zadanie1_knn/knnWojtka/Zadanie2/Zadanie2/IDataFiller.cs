using System;
using System.Collections.Generic;
using System.Text;

namespace Zadanie1
{
    public interface IDataFiller
    {
        void Fill(DataContext context, long howMany);
    }
}
