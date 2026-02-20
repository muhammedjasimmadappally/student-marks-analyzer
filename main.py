students = {}
n = int(input("enter how many students are there: "))
for i in range(n):
  name=input("enter student name here, please: ")
  marks=int(input("enter the marks now, please: "))
  students[name] = marks
print(students)
