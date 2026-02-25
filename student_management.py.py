import os

file_name = "students.txt"

# Add Student
def add_student():

    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    course = input("Enter Course: ")

    file = open(file_name,"a")

    file.write(name+","+roll+","+course+"\n")

    file.close()

    print("Student Added Successfully")


# View Students
def view_students():

    if not os.path.exists(file_name):

        print("No Data Found")
        return

    file=open(file_name,"r")

    data=file.readlines()

    file.close()

    print("\nStudent List\n")

    for line in data:

        name,roll,course=line.strip().split(",")

        print("Name:",name)
        print("Roll:",roll)
        print("Course:",course)
        print("-------------")


# Search Student
def search_student():

    roll=input("Enter Roll Number: ")

    file=open(file_name,"r")

    for line in file:

        name,r,c=line.strip().split(",")

        if roll==r:

            print("\nStudent Found")

            print("Name:",name)
            print("Course:",c)

            file.close()

            return

    file.close()

    print("Student Not Found")


# Delete Student
def delete_student():

    roll=input("Enter Roll Number to Delete: ")

    file=open(file_name,"r")

    data=file.readlines()

    file.close()

    file=open(file_name,"w")

    found=False

    for line in data:

        name,r,c=line.strip().split(",")

        if roll!=r:

            file.write(line)

        else:
            found=True

    file.close()

    if found:
        print("Student Deleted")

    else:
        print("Student Not Found")


# Menu
while True:

    print("\n===== Student Management System =====")

    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 Exit")

    choice=input("Enter Choice: ")


    if choice=="1":
        add_student()

    elif choice=="2":
        view_students()

    elif choice=="3":
        search_student()

    elif choice=="4":
        delete_student()

    elif choice=="5":
        break

    else:
        print("Invalid Choice")