def calculateGPA(score):
    if score >= 80:
        return 4.0
    elif score >= 75:
        return 3.7
    elif score >= 70:
        return 3.3
    elif score >= 65:
        return 3.0
    elif score >= 60:
        return 2.7
    elif score >= 55:
        return 2.3
    elif score >= 50:
        return 2.0
    else:
        return 0.0


def getHonours(gpa):
    if 3.85 <= gpa <= 4.0:
        return "Summa Cum Laude"
    elif 3.70 <= gpa <= 3.84:
        return "Magna Cum Laude"
    elif 3.50 <= gpa <= 3.69:
        return "Cum Laude"
    else:
        return "No Honours"
