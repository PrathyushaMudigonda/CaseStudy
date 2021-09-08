using System;

namespace practise
{
    interface IStudent
    {
        string LibCardNumber
        {
            get;
            set;
        }
        int Year
        {
            get;
            set;
        }
        void Register();
        void PostCourseWork(string work);
    }
    class Employee : IStudent
    {
        string name;
        int year;
        public string LibCardNumber
        {
            get => name;
            set => name = value;
        }
        public int Year
        {
            get => year;
            set => year = value;
        }

        public void Register()
        {
            Console.Write("\nEnter LibCardNumber:");
            string LibCardNumber = Console.ReadLine();
            Console.Write("\nEnter Year:");
            int Year = int.Parse(Console.ReadLine());
            Console.Write("\nYour Details are:");
            Console.WriteLine(LibCardNumber+" "+Year);
        }

        public void PostCourseWork(string work)
        {
            Console.WriteLine("\nYour status is:"+work);
        }
    }
    class EmployeeDisplay
    {
        public static void Main()
        {
            Employee e = new Employee();
            Console.WriteLine("\nEnter Your Details:");
            e.Register();
            Console.Write("\nEnter Post Course Work:");
            string PostCourseworkString = Console.ReadLine();
            e.PostCourseWork(PostCourseworkString);
            Console.ReadLine();
        }

    }
}
