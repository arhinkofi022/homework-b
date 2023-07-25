# Question 2

def calculate_grade(score):
    if score >= 85:
        return "A+", 4.00
    elif score >= 80:
        return "A", 4.00
    elif score >= 75:
        return "B+", 3.50
    elif score >= 70:
        return "B", 3.00
    elif score >= 65:
        return "C+", 2.50
    elif score >= 60:
        return "C", 2.00
    elif score >= 55:
        return "D+", 1.50
    elif score >= 50:
        return "D", 1.00
    else:
        return "E", 0.00

num_score = float(input("Enter numerical score: "))
letter_grade, grade_point = calculate_grade(num_score)
print("Letter Grade:", letter_grade)
print("Grade Point:", grade_point)

def determine_honor(gpa):
    if gpa >= 3.85:
        return "Summa Cum Laude"
    elif gpa >= 3.70:
        return "Magna Cum Laude"
    elif gpa >= 3.50:
        return "Cum Laude"
    else:
        return "None"


cumulative_gpa = float(input("Enter cumulative GPA: "))
honor_category = determine_honor(cumulative_gpa)
print("Honor Category:", honor_category)

def enter_grades():
    num_courses = int(input("Enter the number of courses: "))
    grades_count = {'A+': 0, 'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'E': 0}
    total_credit_points = 0
    total_credits = 0

    for _ in range(num_courses):
        num_score = float(input("Enter numerical score for course {}: ".format(_ + 1)))
        letter_grade, grade_point = calculate_grade(num_score)

        
        grades_count[letter_grade] += 1

        credit_weight = float(input("Enter the credit weighting for course {}: ".format(_ + 1)))
        total_credit_points += grade_point * credit_weight
        total_credits += credit_weight

    cumulative_gpa = total_credit_points / total_credits
    return grades_count, cumulative_gpa


grade_counts, gpa = enter_grades()
print("Grade Counts:", grade_counts)
print("Cumulative GPA:", gpa)

honor_category = determine_honor(gpa)
print("Honor Category:", honor_category)
