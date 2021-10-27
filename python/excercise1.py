#This program is used to compare the three numbers and return the biggest number among those
first_Number=int(input("Enter first number"))  
second_Number=int(input("Enter first number")) 
third_Number=int(input("Enter first number"))  
if (first_Number > second_Number) and (first_Number > third_Number):    #comparing first number with second and third number
    largest=first_Number
elif (second_Number > first_Number) and (second_Number > third_Number):     #comparing second number with first and second number
    largest=second_Number
else:                                                                             
    largest=third_Number
print("The largest of",first_Number,",",second_Number,",",third_Number,"is",largest)
