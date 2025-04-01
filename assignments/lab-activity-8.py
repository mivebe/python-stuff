# def compare_student_courses():
#   # Initialize three empty tuples
#   student1_courses = ()
#   student2_courses = ()
#   shared_courses = ()

#   # Get courses for the first student
#   num_courses1 = int(input("How many courses does the first student have? "))
#   for _ in range(num_courses1):
#     course = input("Enter a course: ")
#     student1_courses += (course,)

#   # Get courses for the second student
#   num_courses2 = int(input("How many courses does the second student have? "))
#   for _ in range(num_courses2):
#     course = input("Enter a course: ")
#     student2_courses += (course,)

#   # Find shared courses
#   for course in student1_courses:
#     if course in student2_courses:
#       shared_courses += (course,)

#   # Display results
#   print(f"Student 1 has {len(student1_courses)} courses: {student1_courses}")
#   print(f"Student 2 has {len(student2_courses)} courses: {student2_courses}")
#   print(f"There are {len(shared_courses)} shared courses: {shared_courses}")

# compare_student_courses()



def process_scores():
  # Initialize an empty list to store scores
  scores = []

  # Get scores from the user
  num_scores = int(input("How many scores would you like to enter? "))
  for _ in range(num_scores):
    score = int(input("Enter a score: "))
    scores.append(score)

  # Display scores in their original order
  print(f"Scores in original order: {scores}")

  # Display scores in order from low to high
  sorted_scores = sorted(scores)
  print(f"Scores from low to high: {sorted_scores}")

  # Find and display the smallest and largest scores
  smallest_score = min(scores)
  largest_score = max(scores)
  print(f"Smallest score: {smallest_score}")
  print(f"Largest score: {largest_score}")

  # Find and display the frequencies of each score
  print("Frequencies of each score:")
  unique_scores = sorted(set(scores))
  for score in unique_scores:
    frequency = scores.count(score)
    print(f"Score {score}: {frequency} time(s)")

# Call the function
process_scores()