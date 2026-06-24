students_marks = {
    "Aditya" : 95,
    "Prathmesh" : 85,
    "Parth" : 75,
    "Abhishekh" : 90,
    "Yashdeep" : 88
}
students_grades = {}

for students in students_marks :
    marks = students_marks[students]
    if marks >= 90:
        students_grades[students] = "A+"
    elif marks >= 80:
        students_grades[students] = "A"
    elif marks >= 70:
        students_grades[students] = "B+"
    elif marks >= 60:
        students_grades[students] = "B"
    elif marks >= 50:
        students_grades[students] = "C"
    elif marks >= 40:
        students_grades[students] = "D"
    else:
        students_grades[students] = "F"
    
print(students_grades)