# Write a menu driven program in Python to do the following operation on “student” table of MySql database "CBSE".

# student table have following field
# student_id          int,  Primary Key,  auto_increment,
# student_name    varchar(30),
# address              varchar(255),
# city                     varchar(30),

# Menu and operation are:
# 1.	Search record based on student_name  field.
# (Ask user to enter name to search)
# 2.	Search record based on city field.
# 3.	Display all record from table.

import mysql.connector


db = mysql.connector.connect(host='localhost',
                             database='school',
                             user='root',
                             password='root')
cursor = db.cursor()
choice = input(
    '1. search record by names\n2. search record by city names\n3. show all data\nchoose one of these options - 1, 2 or 3\n')


def Search(param):
    cursor.execute("select * from student where student_name = " + param)
    All = cursor.fetchall()
    for i in All:
        print(i)


def city(param):
    cursor.execute("select * from student where city = " + param)
    All = cursor.fetchall()
    for i in All:
        print(i)


def disp():
    cursor.execute("select * from student")
    All = cursor.fetchall()
    for i in All:
        print(i)


if choice == '1':
    name = input('enter student name : ')
    Search(name)
elif choice == '2':
    ct = input('enter city name : ')
    city(ct)
elif choice == '3':
    disp()

else:
    print('invalid input')
