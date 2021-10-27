def calc_centuaryAge(age):
   centuary_year=((2021-age)+100)    #subtracting the age from current year and adding 100 to get the centuary age of that person
   return centuary_year

name=input("Enter your name: ")
age=int(input("Enter your age: "))
centuary_year=calc_centuaryAge(age)
print("Hey!! ",name," Now your age is ",age," and you will get 100 in ",centuary_year)
