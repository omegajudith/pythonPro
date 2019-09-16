# #variable
# years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
# ages = []

# #loops thru the years of birth varibale
# for year in years_of_birth:

#     #adds a new year at the end of the year variable
#     ages.append(2014 - year)
#     print(years_of_birth)




import datetime

name = input("Please enter your name")
age = int(input("Please enter your age"))
now_year = int(datetime.date.today().year)

print("Hello " + name + " !")
if age > 100:
  print("You are more than 100 years old. Congrats!")
else:
  print("You'll be 100 years old in " + str(100 - age + now_year))

repetition = int(input("How many times should I repeat the previous message?"))
i = 1
while i <= repetition:
  if age > 100:
    print("You are more than 100 years old. Congrats!")
  else:
    print("You'll be 100 years old in " + str(100 - age + now_year))
  i += 1
