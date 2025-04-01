# # lab-activity-5.py

# # Get input from the user
# start_value = float(input("Enter the start value: "))
# end_value = float(input("Enter the end value: "))
# step_value = float(input("Enter the step value: "))

# # Print the table header
# print(f"{'Pounds':>10} {'Ounces':>15} {'Grams':>15}")
# print("-" * 40)

# # Loop through the range of values
# for unit in range(int(start_value * 10), int(end_value * 10) + 1, int(step_value * 10)):
#   unit = unit / 10  # Convert back to float
#   ounces = unit * 16  # Convert pounds to ounces
#   grams = unit * 453.592  # Convert pounds to grams
  
#   # Print the row with right-aligned values
#   print(f"{unit:10.1f} {ounces:15.1f} {grams:15.1f}")

# Get the number of days from the user
num_days = int(input("Enter the number of days: "))

# Initialize variables
total_speed = 0
min_speed = float('inf')
max_speed = float('-inf')

# Loop to get wind speed for each day
for day in range(1, num_days + 1):
  speed = float(input(f"Enter the maximum wind speed for day {day} (in km/h): "))
  total_speed += speed
  if speed < min_speed:
    min_speed = speed
  if speed > max_speed:
    max_speed = speed

# Calculate the average speed
average_speed = total_speed / num_days

# Display the results
print(f"\nMinimum Speed: {min_speed:.1f} km/h")
print(f"Maximum Speed: {max_speed:.1f} km/h")
print(f"Average Speed: {average_speed:.1f} km/h")