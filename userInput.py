
# Here we can get some input results


calculation_to_units= 24
name_to_units = "hrs"

def days_to_unit(no_of_days):
    print(f"{no_of_days} days are {no_of_days * calculation_to_units} {name_to_units}")
    print("All good ")

user_input= input("Please insert the number of days  we will give you the result \n")
userInput= int(user_input)

calculate = days_to_unit(userInput)
print(calculate)
