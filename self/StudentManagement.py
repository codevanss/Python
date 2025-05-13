class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}")

    def update_course(self, new_course):
        self.course = new_course
        print(f"✅ Course updated to {self.course}")


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student
        print(f"✅ Student {student.name} added.")

    def view_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            student.display_info()
        else:
            print("❌ Student not found.")

    def update_student_course(self, student_id, new_course):
        student = self.students.get(student_id)
        if student:
            student.update_course(new_course)
        else:
            print("❌ Student not found.")


# Example usage
if __name__ == "__main__":
    manager = StudentManager()

    while True:
        print("\n1. Add Student\n2. View Student\n3. Update Course\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            s_id = input("Enter student ID: ")
            name = input("Enter name: ")
            course = input("Enter course: ")
            student = Student(s_id, name, course)
            manager.add_student(student)

        elif choice == "2":
            sid = input("Enter student ID to view: ")
            manager.view_student(sid)

        elif choice == "3":
            sid = input("Enter student ID to update: ")
            new_course = input("Enter new course: ")
            manager.update_student_course(sid, new_course)

        elif choice == "4":
            print("👋 Exiting Student Management System.")
            break

        else:
            print("❌ Invalid choice. Try again.")
