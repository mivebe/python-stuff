# # Program to take user input for personal details and display them with descriptive messages

# def program1()1:
#   # Prompt user for each input and store it in variables
#   first_name = input("Enter your first name: ")
#   last_name = input("Enter your last name: ")
#   faculty = input("Enter your faculty: ")
#   year_of_study = input("Enter your year of study: ")
#   dob_month = input("Enter your birth month: ")
#   dob_day = input("Enter your birth day: ")
#   dob_year = input("Enter your birth year: ")

#   # Display each item with a descriptive message
#   print("\n--- Your Information ---")
#   print("First Name: " + first_name)
#   print("Last Name: " + last_name)
#   print("Faculty: " + faculty)
#   print("Year of Study: " + year_of_study)
#   print("Date of Birth: " + dob_month + " " + dob_day + ", " + dob_year)


# # Prompt user for course details
# def program2():
#   course_name = input("Enter a course name: ")
#   course_number = input("Enter a course number: ")
#   course_section = input("Enter a course section: ")
#   semester = input("Enter a semester (Winter, Summer): ")
#   year = input("Enter a year: ")

#   # Words to skip when extracting initials
#   skip_words = {"and", "of", "in", "the", "for", "on", "at", "to", "with"}

#   # Extract initials from course name, skipping specified words
#   course_initials = ''.join(
#       word[0].upper() for word in course_name.split() 
#       if word.isalpha() and word.lower() not in skip_words
#   )

#   # Generate course code
#   course_code = f"{course_initials}{course_number.upper()}{course_section.upper()}{year}"

#   # Display the course code
#   print(f"The course code is {course_code}")

# def main():
#   print("Choose a program to run:")
#   print("1. Program One")
#   print("2. Program Two")
#   choice = input("Enter your choice (1 or 2): ")

#   if choice == "1":
#     program1()
#   elif choice == "2":
#     program2()
#   else:
#     print("Invalid choice. Please run the program again and select 1 or 2.")

# if __name__ == "__main__":
#   main()




def calculate_weighted_grade(grade, weight):
  return grade * weight

def calculate_final_grade(weighted1, weighted2, weighted3, weighted4):
  return weighted1 + weighted2 + weighted3 + weighted4

# Input grades for four items
grade1 = float(input("Enter the grade for item 1: "))
grade2 = float(input("Enter the grade for item 2: "))
grade3 = float(input("Enter the grade for item 3: "))
grade4 = float(input("Enter the grade for item 4: "))

# Define weights for each grade
weight1 = 0.15
weight2 = 0.20
weight3 = 0.25
weight4 = 0.40

# Calculate weighted grades
weighted1 = calculate_weighted_grade(grade1, weight1)
weighted2 = calculate_weighted_grade(grade2, weight2)
weighted3 = calculate_weighted_grade(grade3, weight3)
weighted4 = calculate_weighted_grade(grade4, weight4)

# Calculate final grade
final_grade = calculate_final_grade(weighted1, weighted2, weighted3, weighted4)

# Display results
print(f"Weighted grade for item 1: {weighted1:.1f}")
print(f"Weighted grade for item 2: {weighted2:.1f}")
print(f"Weighted grade for item 3: {weighted3:.1f}")
print(f"Weighted grade for item 4: {weighted4:.1f}")
print(f"Final weighted grade: {final_grade:.1f}")