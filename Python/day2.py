class Student:
	def __init__(self, firstname , lastname):
		self.firstname = firstname
		self.lastname = lastname

class StudentManagement:

	students = list()

	def __init__(self):
		self.students.append(Student("oğuzhan", "öksel"))
		self.students.append(Student("praesent", "blandit"))
		self.students.append(Student("commodo", "elit"))

	def add_student(self, firstname, lastname):
		self.students.append(Student(firstname, lastname))

	def add_range_student(self, student_list):
		for student in student_list:
			self.students.append(student)

	def remove_student(self, firstname, lastname):
		for student in self.students:
			if student.firstname == firstname and student.lastname == lastname:
				self.students.remove(student)

	def remove_range_student(self, student_list):
		for student in student_list:
			self.students.remove(student)
	
	def print_list(self):
		print("\n")
		for student in self.students:
			print(f"firstname: {student.firstname} lastname: {student.lastname}")
	
	def get_index(self, student):
		idx = 0
		while idx < len(self.students):
			if student is self.students[idx]:
				print(f"index of {self.students[idx].firstname},{idx}")
			idx += 1



student_management = StudentManagement()
new_student = Student("abc", "abc")
new_student_list = [
		Student("Quisque", "pellentesque"),
		Student("ante", "dui"),
		Student("pharetra", "fermentum"),
	]

student_management.print_list()
student_management.add_student(new_student)
student_management.print_list()
student_management.get_index(new_student)


