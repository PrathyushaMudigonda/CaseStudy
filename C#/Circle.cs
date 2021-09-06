using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace arrays
{
    class Circle
    { 
            double Radius;
            public void setRadius(double Radius)
            {
                this.Radius = Radius;
            }
            public double getRadius()
            {
                return this.Radius;
            }
            public double calcDiameter()
            {
                double diameter = 2 * Radius;
                return diameter; 
            }
            public double calcArea()
            {
                double area = Math.PI * Radius * Radius;
                return area;
            }
    }
    class CircleValues
    {
        public static void Main()
        {
            Console.WriteLine("Enter Radius:");
            double Radius = double.Parse(Console.ReadLine());
            Circle circle = new Circle();
            circle.setRadius(Radius);
            Console.Write("Entered Radius value is:");
            Console.WriteLine(circle.getRadius());
            Console.Write("Diameter of circle is:");
            Console.WriteLine(circle.calcDiameter());
            Console.Write("Area of the circle is:");
            Console.WriteLine(circle.calcArea());
            Console.ReadLine();
        } 
    }
}