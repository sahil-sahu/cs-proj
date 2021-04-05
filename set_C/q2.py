import mysql.connector
con = mysql.connector.connect(
    host="KV-LL-22", user="kv6", password="kv6", database="CBSE")
c = con.cursor()
choice = input('1. show total marks by names\n2. show name of student with highest cs mark\n3. students having cs marks more than maths\nchoose one of these options - 1, 2 or 3\n')
if choice == '1':
    c.execute(
        'select student_name, sum(eng,phy,chem,math,cs) as total from student_marks;')
    n = c.fetchall()
    for i in n:
        print(i)
elif choice == '2':
    ct = input('enter city name : ')
    c.execute('select student_name,max(cs) from student ;')
    high = c.fetchone()
    print(high)
elif choice == '3':
    c.execute('select * from student where cs > math;')
    All = c.fetchall()
    for i in All:
        print(i)
else:
    print('invalid input')
con.commit()
#c.execute("CREATE DATABASE if not exists CBSE")
#c.execute('create table if not exists student (student_id int AUTO_INCREMENT PRIMARY KEY,student_name varchar(30),address varchar(255),city varchar(30))')
#c.execute('INSERT INTO student (student_name, address, city) VALUES (%s, %s, %s)',(name,address,city))
