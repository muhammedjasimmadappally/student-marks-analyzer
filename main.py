def main():
 students = {}
 n = int(input("enter how many students are there: "))
 for i in range(n):
   name=input("enter student name here, please: ")
   marks=int(input("enter the marks now, please: "))
   students[name] = marks

 total = 0
 topper=""
 highest_mark=-1
 failed_students=[]

 for name,mark in students.item():
   total+=mark

   if marks> highest_mark:
     highest_mark=mark
     topper=name

   if mark<40:
     failed_students.append(name)
 average=total/n

 print("Average Marks:", average)
 print("Topper:", topper, "-", highest_marks)
 print("Failed Students:", failed_students)
if __name__ == "__main__":
    main()
