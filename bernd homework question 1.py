# the weights
hwWeight = 0.4
examWeight = 0.5
discussionWeight = 0.1

# ask user for grades
homework_grade = float(input("Enter your homework grade: "))
exam_grade = float(input("Enter your exam grade: "))
discussion_grade = float(input("Enter your discussion grade: "))

# Compute the weighted grade
weighted_grade = (homework_grade * hwWeight) + (exam_grade * examWeight) + (discussion_grade * discussionWeight)

# Print the total grade
print("Your total grade is:", weighted_grade)
