from datetime import datetime

user_input = input("Enter your goal with dead line separated with deadline(ex: demo:15:04:2022):\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

# Calculate how many days from now till deadline
time_till = deadline_date - today_date

# Calculate how many hours from now till deadline
hours_till = int(time_till.total_seconds() / 60 / 60)

print(f"Dear user! Time remaining for your goal {goal} is {hours_till} hours.")
