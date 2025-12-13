import csv 

# Create a Student class
class Student:
	def __init__(self, name, age, class_name):
		self.name = name
		if age < 0:
			raise Exception("Age can't be negative")
		self.age = age
		self.class_name = class_name
		self.marks = {}
	
	def get_name(self):
		return self.name
	
	def get_marks(self):
		print("#"*30)
		for subject, mark in self.marks.items():
			print(subject, mark)
	
	def set_mark(self, subject, mark):
		if mark < 0:
			raise Exception("Mark Can't Be Negative")
		if subject.strip() == "":
			raise Exception("Subject name can't be empty")
		self.marks[subject] = mark
	
# Create a Grading System class
class GradingSystem:
	
	def __init__(self):
		self.students = []
	
	def add_student(self, student):
		self.students.append(student)
	
	def get_students_of_class(self, class_name):
		result = []
		for student in self.students:
			if student.class_name == class_name:
				result.append(student.name)
		return result
	
	def get_students_avg_mark(self, subject, class_name):
		total = 0
		total_students = 0
		for student in self.students:
			if student.class_name == class_name:
				total = total + student.marks.get(subject, 0)
				total_students = total_students + 1
		avg_mark = total / total_students
		print(f"Average marks for {subject} under {class_name} is {avg_mark}")
	
	def export_to_csv(self, class_name):
		# Filter 
		filtered_students = []
		for student in self.students:
			if student.class_name == class_name:
				filtered_students.append(student)
		
		# Write to CSV
		filename = f"export_of_{class_name.replace(' ', '_')}.csv"
		with open(filename, "w") as f:
			writer = csv.writer(f)
			writer.writerow(["class_name", "student_name", "age", "math", "science"])
			
			for student in filtered_students:
				writer.writerow([student.class_name, student.name, student.age, student.marks.get("Maths"), student.marks.get("Science")])

students_list = [
	["Syed Jafer", -28, '10th']
]

students = []
for element in students_list:
	try:
		obj = Student(element[0], element[1], element[2])
		students.append(obj)
	except Exception as ex:
		print(ex)		
try:
	syed = Student("Syed Jafer", 28, '10th')
	syed.set_mark("Maths", 78)
	syed.set_mark("Science", -35)
	syed.set_mark("Social", 35)
	syed.set_mark("Tamil", 44)
	syed.set_mark("English", 40)
except Exception as ex:
	print(ex)

# Create objects and assign values
kingsley = Student("kingsley", 30, '12th')
kingsley.set_mark("Maths", 45)
kingsley.set_mark("Science", 35)
kingsley.set_mark("Social", 35)
kingsley.set_mark("Tamil", 44)
kingsley.set_mark("English", 40)

vignesh = Student("Vignesh", 35, '12th')
vignesh.set_mark("Maths", 95)
vignesh.set_mark("Science", 45)
vignesh.set_mark("Social", 35)
vignesh.set_mark("Tamil", 44)
vignesh.set_mark("English", 49)

wijay = Student("Wijay", 28, '12th')
wijay.set_mark("Maths", 65)
wijay.set_mark("Science", 75)
wijay.set_mark("Social", 85)
wijay.set_mark("Tamil", 44)
wijay.set_mark("English", 40)

arun = Student("Arun", 28, '12th')
arun.set_mark("Maths", 95)
arun.set_mark("Science", 85)
arun.set_mark("Social", 95)
arun.set_mark("Tamil", 94)
arun.set_mark("English", 40)

gs = GradingSystem()
gs.add_student(syed)
gs.add_student(kingsley)
gs.add_student(vignesh)
gs.add_student(arun)
gs.add_student(wijay)

# Use methods to get student's average marks
gs.get_students_avg_mark("Maths", "10th")

# Export data to csv file
gs.export_to_csv("12th")

