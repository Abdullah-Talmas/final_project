import uuid

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark


course_name = input("Enter course name: ")
course_mark = float(input("Enter course mark: "))

course = Course(course_name, course_mark)

print("Course ID:", course.course_id)
print("Course Name:", course.course_name)
print("Course Mark:", course.course_mark)

class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print("Course Name:", course.course_name)
            print("Course Mark:", course.course_mark)
            print()

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        average = total_marks / len(self.courses_list) if self.courses_list else 0
        return average


students = []  # TODO 8 declare empty students list

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"))  # TODO 9 handle Exception for selection input

        if selection == 1:
            student_number = input("Enter Student Number: ")

            # TODO 10 make sure that Student number is not exists before
            existing_student = next((student for student in students if student.student_number == student_number), None)
            if existing_student:
                print("Student Number already exists. Please try again.")
                continue

            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value")

            new_student = Student(student_name, student_age, student_number)  # TODO 11 create student object
            students.append(new_student)

            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            target_student = None

            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                students.remove(target_student)
                print("Student Deleted Successfully")
            else:
                print("Student Not Found")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            target_student = None

            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                print("Student Details:")
                print(target_student.get_student_details())
            else:
                print("Student Not Found")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            target_student = None

            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                average = target_student.get_student_average()
                print("Student Average:", average)
            else:
                print("Student Not Found")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            target_student = None

            for student in students:
                if student.student_number == student_number:
                    target_student = student
                    break

            if target_student:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                new_course = Course(course_name, course_mark)
                target_student.enroll_course(new_course)
                print("Course Added to Student Successfully")
            else:
                print("Student Not Found")

        elif selection == 6:
            # TODO 16 call a function to exit the program
            break

        else:
            print("Invalid Selection. Please try again.")

    except ValueError:
        print("Invalid Input. Please enter a number.")

