#---------Project: Student Management System (with File & Exception Handling)-----------
#(1.) To Add Students Records.
#(2.) To View Students Lists.
#(3.) To Search Students By Roll Number.
#(4.) To Delete Students Details.
#(5.) To Handle Error.

import os

Filename='students.txt' #storing students data.


# To Add Students Records:-
def Add_Students():
    try:
        roll=int(input('Enter your roll number:'))
        name=input('Enter your name:')
        marks=input('Enter your marks:')

        with open('students.txt',mode='a') as f:
            f.write(f"{roll},{name},{marks}\n")
        print('students added successfully!')

    except Exception as var:
        print('Error while adding students:',var)

# To View Students Records:-
def view_students():
    try:
        with open('students.txt',mode='r') as f:
            data=f.readlines()
            if not data:
                print('No records found!')
            for line in data:
                roll,name,marks=line.strip().split(",")
                print(f"Roll:{roll} | name:{name} | marks:{marks}")
    except FileNotFoundError:
        print('File not found! Add some students first.')

# To Search Students By The Roll Number:-
def search_students():
    try:
        roll_search=input('Enter the students roll number:')
        found=False

        with open('students.txt',mode='r') as f:
            for line in f:
                roll,name,marks=line.strip().split(",")
                if roll==roll_search:
                    print(f"Found: Roll{roll},Name:{name},Marks:{marks}")
                    found=True
                    break
        if not found:
            print("students not found!")

    except FileNotFoundError:
        print("File not found! Add some students first.")

# To Delete Students Records:-
def delete_students():
    try:
        roll_delete=int(input('Enter roll number to delete:'))
        updated_data=[]
        deleted=False

        with open('students.txt',mode='a') as f:
            for line in f:
                roll, name, marks=line.strip().split(",")
                if roll!=roll_delete:
                    updated_data.append(line)
                else:
                    deleted=True

        if deleted:
            with open('students.txt',mode='a') as f:
                f.writelines(updated_data)
            print('students deleted successfully!')

        else:
            print('student not found')

    except FileNotFoundError:
        print("File not found! Add some students first. ")

while True:
    print('Welcome Student Management System')
    print('1.To Add Students Records:-')
    print('2.To View Students Records:-')
    print('3.To Search Students By The Roll Number:-')
    print('4.To Delete Students Records:-')
    print('5.Exit')

    try:

        choise=int(input("Enter your choise"))

        if choise==1:
            print(Add_Students())
        elif choise==2:
            print(view_students())
        elif choise==3:
            print(search_students())
        elif choise==4:
            print(delete_students())
        else:
            if choise==5:
                print('Thanku')
                break
    except ValueError:
        print('Invalid input! Please enter a number.')


