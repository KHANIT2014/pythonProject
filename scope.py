# A variable is only avaiable inside from the region it is created


calculation_to_units = 24
name_to_units = "hrs"


def days_to_unit(no_of_days):
    print(f"{no_of_days} days are {no_of_days * calculation_to_units} {name_to_units}")
    print("All good ")


def  scope_define(no_of_days):
    print(name_to_units)
    print(no_of_days)


scope_define(20)


# scope variable is mentioned in global and non global




