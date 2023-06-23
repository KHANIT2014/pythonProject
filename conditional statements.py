
# Here we can get some input results


calculation_to_units= 24
name_to_units = "hrs"


# we have added if else statement if means match then print else means if not match then print this
def days_to_unit(no_of_days):
    if no_of_days >0:
        print(f"{no_of_days} days are {no_of_days * calculation_to_units} {name_to_units}")

    else:
        return "you have entered negative value there is no result for you.."

    print("All good ")

user_input= input("Please insert the number of days  we will give you the result \n")
userInput= int(user_input)

calculate = days_to_unit(userInput)
print(calculate)

# we have added if  elif else statement if means match then print elif then print this  else means if not match then print this
def days_to_unit(no_of_days):
    if no_of_days >0:
        print(f"{no_of_days} days are {no_of_days * calculation_to_units} {name_to_units}")

    elif no_of_days == 0:
        return "you have enter 0 please enter above the 0 it  will show results"

    else:
        return "you have entered negative value there is no result for you.."

    print("All good ")

user_input= input("Please insert the number of days  we will give you the result \n")
userInput= int(user_input)

calculate = days_to_unit(userInput)
print(calculate)
