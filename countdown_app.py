from datetime  import datetime


user_goal = input( " Please Let me know your goal with a deadline, seperated with a colon \n")
input_list = user_goal.split(":")

goal = input_list[0]
dead_line = input_list[1].strip()

try_int = input_list[1]
print(dead_line)
print(input_list)

# print(datetime.datetime.strptime(dead_line, "%d.%m.%Y"))


format_data = "%d.%m.%Y"

#Run the datetime format with the string given in the [1] list variable
date = datetime.strptime(dead_line, format_data)
# print(date)

# Calculate how many days till the deadline
today = datetime.today()
target_goal = date - today

# Calculating Total Hours Till Target Date
hours_til = target_goal.total_seconds()/60/60
print(round(hours_til))


print(f"Hey Buddy, You have {target_goal.days} days to reach your target '{goal}'.Keep Going, You Got This!")

print(f"Hey Buddy, You have {int(hours_til)} Hours to reach your target '{goal}'.Keep Going, You Got This!")



