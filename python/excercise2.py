#This program is used to compare the three numbers and return the biggest number among those
def calc_biggestNumber(first_Number,second_Number,third_Number):
    if (first_Number > second_Number) and (first_Number > third_Number):       #comparing first number with second and third number
          return first_Number
    elif (second_Number > first_Number) and (second_Number > third_Number):      #comparing second number with first and second number
          return second_Number
    else:
          return third_Number

first=int(input("Enter first number: "))        
second=int(input("Enter second number: "))      
third=int(input("Enter third number: "))       
largest=calc_biggestNumber(first,second,third)
print("The largest of",first,",",second,",",third,"is",largest)
