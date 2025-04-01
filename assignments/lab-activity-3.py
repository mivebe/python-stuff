# # Function to calculate the total daytime and nighttime
# def calculate_daytime_nighttime():
#     # Get sunrise and sunset times from the user
#     sunrise_hour = int(input("Enter the sunrise hour (0-23): "))
#     sunrise_minute = int(input("Enter the sunrise minute (0-59): "))
#     sunset_hour = int(input("Enter the sunset hour (0-23): "))
#     sunset_minute = int(input("Enter the sunset minute (0-59): "))
    
#     # Convert sunrise and sunset times to minutes since midnight
#     sunrise_total_minutes = sunrise_hour * 60 + sunrise_minute
#     sunset_total_minutes = sunset_hour * 60 + sunset_minute
    
#     # Calculate the total daylight time in minutes
#     daylight_minutes = sunset_total_minutes - sunrise_total_minutes
    
#     # Calculate total daytime in hours and remaining minutes
#     daylight_hours = daylight_minutes // 60
#     daylight_remaining_minutes = daylight_minutes % 60
    
#     # Calculate total nighttime in minutes
#     nighttime_minutes = 1440 - daylight_minutes  # Total minutes in 24 hours is 1440
    
#     # Calculate total nighttime in hours and remaining minutes
#     nighttime_hours = nighttime_minutes // 60
#     nighttime_remaining_minutes = nighttime_minutes % 60
    
#     # Display the results
#     print(f"Daytime: {daylight_hours} hours and {daylight_remaining_minutes} minutes")
#     print(f"Nighttime: {nighttime_hours} hours and {nighttime_remaining_minutes} minutes")

# # Call the function
# calculate_daytime_nighttime()




def main():
    # Ask the user for the number of coins of each type
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))
    loonies = int(input("Enter the number of loonies: "))
    twonies = int(input("Enter the number of twonies: "))
    
    # Calculate the total value for each type of coin
    value_nickels = nickels * 0.05
    value_dimes = dimes * 0.10
    value_quarters = quarters * 0.25
    value_loonies = loonies * 1
    value_twonies = twonies * 2
    
    # Calculate the total sum of all the coin values
    total_value = value_nickels + value_dimes + value_quarters + value_loonies + value_twonies
    
    # Display the results, formatted to two decimal places
    print(f"\nValue of nickels: ${value_nickels:.2f}")
    print(f"Value of dimes: ${value_dimes:.2f}")
    print(f"Value of quarters: ${value_quarters:.2f}")
    print(f"Value of loonies: ${value_loonies:.2f}")
    print(f"Value of twonies: ${value_twonies:.2f}")
    print(f"Total value of all coins: ${total_value:.2f}")

if __name__ == "__main__":
    main()
