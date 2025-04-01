# # Program to take user input for personal details and display them with descriptive messages

# # Prompt user for each input and store it in variables
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# faculty = input("Enter your faculty: ")
# year_of_study = input("Enter your year of study: ")
# dob_month = input("Enter your birth month: ")
# dob_day = input("Enter your birth day: ")
# dob_year = input("Enter your birth year: ")

# # Display each item with a descriptive message
# print("\n--- Your Information ---")
# print("First Name: " + first_name)
# print("Last Name: " + last_name)
# print("Faculty: " + faculty)
# print("Year of Study: " + year_of_study)
# print("Date of Birth: " + dob_month + " " + dob_day + ", " + dob_year)




# Prompt user for course details
course_name = input("Enter a course name: ")
course_number = input("Enter a course number: ")
course_section = input("Enter a course section: ")
semester = input("Enter a semester (Winter, Summer): ")
year = input("Enter a year: ")

# Words to skip when extracting initials
skip_words = {"and", "of", "in", "the", "for", "on", "at", "to", "with"}

# Extract initials from course name, skipping specified words
course_initials = ''.join(
    word[0].upper() for word in course_name.split() 
    if word.isalpha() and word.lower() not in skip_words
)

# Generate course code
course_code = f"{course_initials}{course_number.upper()}{course_section.upper()}{year}"

# Display the course code
print(f"The course code is {course_code}")