import mysql.connector
con = mysql.connector.connect(
    host="KV-LL-22", user="kv6", password="kv6", database="CBSE")
c = con.cursor()
c.execute('create table if not exists employee (employee_id int AUTO_INCREMENT PRIMARY KEY,employee_name varchar(30),employee_address varchar(255),employee_city varchar(30))')
choice = input(
    '1. insert record\n2. show all data\nchoose one of these options - 1 or 2\n')
if choice == '1':
    name = input('enter emloyee name : ')
    address = input('enter emloyee address : ')
    city = input('enter emloyee city : ')
    c.execute('INSERT INTO student (emp_name, emp_address, emp_city) VALUES (%s, %s, %s);',
              (name, address, city))
    print('record inserted successfully')
elif choice == '2':
    c.execute('select * from employee;')
    All = c.fetchall()
    for i in All:
        print(i)
else:
    print('invalid input')
con.commit()
