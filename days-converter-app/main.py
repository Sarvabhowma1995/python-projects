from days_converter import validate_user_data, user_input_message  # this is to import only none function and variable
# import days_converter #this is to import entire module
# from days_converter import *  #This will help us to import all functions and variables from module
# from days_converter import validate_user_data as test    ## this will import with test name instead of actual name


user_data = ""
while user_data != "exit":
    user_data = input(user_input_message)
    user_data_dict = {"days": user_data.split(":")[0], "unit": user_data.split(":")[1]}
    validate_user_data(user_data_dict)

