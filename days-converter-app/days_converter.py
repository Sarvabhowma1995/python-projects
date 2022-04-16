user_input_message = "Please provide number of days with comma separated to convert:\n"


def days_to_units(no_of_days, user_unit):
    if user_unit == "hours":
        return f"{no_of_days} Days are {no_of_days * 24} {user_unit} \n"
    elif user_unit == "minutes":
        return f"{no_of_days} Days are {no_of_days * 24 * 60} {user_unit} \n"
    elif user_unit == "seconds":
        return f"{no_of_days} Days are {no_of_days * 24 * 60 * 60} {user_unit} \n"
    else:
        return "Unsupported Unit"


def validate_user_data(user_data_dict):
    try:
        user_input_data = int(user_data_dict["days"])
        if user_input_data > 0:
            print(days_to_units(user_input_data, user_data_dict["unit"]))
        elif user_input_data == 0:
            print("You entered zero, So please enter the valid positive numbers.\n")
        elif user_input_data != int:
            print("it's a negative value, So please enter the valid positive numbers.\n")
    except ValueError:
        print("Your input is not a valid number, Please provide the valid positive numbers.\n")
