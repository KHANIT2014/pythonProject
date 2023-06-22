print("Hi, World this is khan javid")
print ("20 Days are "+ str(50) + ( " minutes")  )



calculation_to_units= 24
name_to_units= "hrs"

def days_to_unit(no_of_days):
    print(f"{no_of_days} days are {no_of_days * calculation_to_units} {name_to_units}")
    print("All good ")


days_to_unit(50)


def days_to_unit(no_of_days):
    print(f"{no_of_days} days are {no_of_days * calculation_to_units} {name_to_units}")
    print("All good ")


days_to_unit(50)
days_to_unit(510)
days_to_unit(530)
days_to_unit(500)



# Here we are adding prameter, make sure that once you done define the pramater e.g custom_message. i have define it
def days_to_unit(no_of_days,custom_message):
    print(f"{no_of_days} days are {no_of_days * calculation_to_units} {name_to_units}")
    print(custom_message)


days_to_unit(50, "Here we have added some prameters ")


