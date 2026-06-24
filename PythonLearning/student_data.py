student_data = [
    {
        "Name" : "Ram",
        "Age" : 19,
        "Roll" : 25,
    },
    {
        "Name" : "Shyam",
        "Age" : 20,
        "Roll" : 30,
    },
]
def add_new_data(name,age,roll):
    new_student = {}
    new_student["Name"] = name
    new_student["Age"] = age
    new_student["Roll"] = roll
    student_data.append(new_student)

add_new_data(name = "Aditya",age = 25,roll = 45)
print(student_data)

