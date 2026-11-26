#1.add students..
students=[]
def add():
    s_id=int(input("Enter Student ID:"))
    name=input("Enter Student Name:")
    s_age=int(input("Enter Student Age:"))
    s_course=input("Enter Student Course:")
    s_marks=int(input("Enter Student Marks:"))

    student={
        "id":s_id,
        "name":name,
        "age":s_age,
        "course":s_course,
        "marks":s_marks
        }
    students.append(student)
    print("sucessfully added students")
    
#2.display all students..        
def display():
    print("all students")
    if len(students)==0:
        print("No record found")
        return
    
    for student in students:
        print("s_id:",student["id"])
        print("name:",student["name"])
        print("age:",student["age"])
        print("course:",student["course"])
        print("marks:",student["marks"])
        
            
#3.search students..        
def search():
    print("search student..")
    s_id=int(input("Enter Student ID:"))
    for student in students:
        if student["id"]==s_id:
            print("student found")
            print("Student_id:",student["id"])
            print("name:",student["name"])
            print("age:",student["age"])
            print("course:",student["course"])
            print("marks:",student["marks"])
        
            return
        print("Student Not Found")

#4.update student..
def update():
    print("update student..")
    s_id=int(input("Enter Student ID:"))
    for student in students:
        if student["id"]==s_id:
            print("enter new details:")
            student["name"]=input("Enter Name:")
            student["s_age"]=int(input("Enter Age:"))
            student["s_course"]=input("Enter Course:")
            student["s_marks"]=int(input("Enter Marks:"))
            return
        print("student not found")
    

#5.delete function        
def delete():
    print("----------delete student--------")

    s_id=int(input("Enter Student ID:"))

    for student in students:
        if student["id"]==s_id:
            students.remove(student)

            print("student deletes successfully..")
            return
        print("student not found")
        

#6.calculate result    
def calculate():
    print("----------student result-----------")

    s_id=int(input("Enter Student ID:"))
    for student in students:
        if student["id"]==s_id:
            marks=student["Marks"]
            
            if marks>=90:
                grade="A+"
            elif marks>=80:
                grade="A"
            elif marks>=70:
                grade="B"
            elif marks>=60:
                grade="C"
            elif marks>=50:
                grade="D"
            else:
               grade="F"

               print("-------------")
               print("s_id:",student["id"])
               print("name:",student["name"])
               print("marks:",student["marks"])
               print("grade:",student["grade"])

            if marks>=40:
                print("result:",PASS)
            else:
                print("result:",FAIL)
            return
        print("student not found")
               
#main program    
while True:
    print("\n---------Student Result Analyzer--------------")
    print("1.add student")
    print("2.Display student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.calculate student")
    print("7.Exit")

    choice=int(input("Enter Youe Choice:"))

    if choice==1:
         add()
    elif choice==2:
        display()
    elif choice==3:
        search()
    elif choice==4:
        update()
    elif choice==5:
        delete()
    elif choice==6:
        calculate()
    elif choice==7:
        print("Thank You using student management system")
      
    else:
        print("Inavalid choice")

























    
