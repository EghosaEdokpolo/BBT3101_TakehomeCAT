class Student:
    def __init__(self, name, student_id):
        self.iname = name
        self.istudent_id = student_id
        self.assignments_list = {}

    def add_assignment(self):
        idx = 2
        while idx:
            idx -= 1
            inp_asgnname = input("what is the assignment name? ")
            inp_asgngrade = input("what is the grade? ")

            self.assignments_list.update({inp_asgnname: inp_asgngrade})
    
    def display_grade(self):
        return self.assignments_list

            

class Instructor:
    def __init__(self, name, course_name):
        self.iname = name
        self.icourse_name = course_name
        self.studentlist = []

    def add_student(self):
        inp_studname = input("what is your name? ")
        inp_studid = input("what is your id? ")

        new_student = Student(inp_studname, inp_studid)

        self.studentlist.append(new_student)
        print(f"\nStudent: {inp_studname}, {inp_studid} added to {self.icourse_name}.")

    def assign_grade(self, position):
        self.studentlist[position].add_assignment()

    def display_all(self):
        for student in self.studentlist:
            print(f"{student.iname}, {student.istudent_id}, {student.display_grade()}")


    #execution
nw_instructor = Instructor("james", "calculus")
nw_instructor.add_student()
nw_instructor.add_student()
nw_instructor.assign_grade(0)
nw_instructor.assign_grade(1)

nw_instructor.display_all()

