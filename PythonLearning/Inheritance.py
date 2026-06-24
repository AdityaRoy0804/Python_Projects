class University:
    def __init__(self):
        self.name = "YCCE"
    
    def show(self):
        print(f"University Name: {self.name}")

class Courses(University):
    def __init__(self):
        super().__init__()  # Use super() to avoid multiple University instances
        self.course = "Machine Learning"
    
    def display(self):
        print(f"Course name: {self.course}")

class Branch(University):
    def __init__(self):
        super().__init__()
        self.branch = "AIDS"
    
    def put(self):
        print(f"Branch name: {self.branch}")

class Students(Branch, Courses):  # Maintain proper MRO
    def __init__(self):
        super().__init__()  # Ensures proper initialization in MRO
        self.student = "Aditya Kumar Roy"
    
    def show_name(self):
        self.show()     # Correct method calls
        self.display()
        self.put()
        print(f"Student name: {self.student}")

class Faculty(Branch):
    def __init__(self):
        super().__init__()  # Corrected super() usage
        self.faculty = "Andrew"
    
    def show_faculty(self):
        self.show()     # Correct method calls
        self.put()
        print(f"Faculty name: {self.faculty}")

# Creating a student object and displaying details
student_1 = Students()
student_1.show_name()

faculty_1 = Faculty()
faculty_1.show_faculty()