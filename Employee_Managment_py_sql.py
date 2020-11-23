#***************The database will be saved in your current working directory*****************
#***************Databse name Employee_managment.db**********************


"""Importing required libraries"""
import sqlite3

"""Creating a connection with the local data base file"""
connection = sqlite3.connect("Employee_managment.db")
cursor = connection.cursor()

"""Below code will check if the table already exist or not and create new one if it dosent"""
cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='employee';""")
if cursor.fetchone()[0]==1 :
    pass
else:
    sql_command = """CREATE TABLE employee (
    emp_ID VARCHAR(20) PRIMARY KEY, 
    first_name VARCHAR(20), 
    last_name VARCHAR(30), 
    gender CHAR(1), 
    salary INTEGER,
    birth_date DATE);"""
    cursor.execute(sql_command)
    connection.commit()

"""The local data base is created and the table employee is added to it."""

"""Method to enter data into table"""


def employee_add(e_id, fname, lname, gender, salary, dob):
    try:
        cursor.execute("""INSERT INTO employee(emp_ID, first_name, last_name, gender,salary, birth_date) 
                        VALUES(?,?,?,?,?,?)""", (e_id, fname, lname, gender, salary, dob))
        print("Employee Added\n")
        show_all()
        connection.commit()
    except:
        print("Employee with employee Id :"+e_id +" Already exist")


"""Method to search an employee"""


def find_emp_id(emp_id):
    cursor.execute("""SELECT * FROM employee
                WHERE emp_ID = ?""", (emp_id,))
    result = cursor.fetchall()
    if not result:
        print("Employee not FOUND !!!!")
    else:
        for row in result:
            print("Employee_ID :", row[0])
            print("First_name  :", row[1])
            print("Last_name   :", row[2])
            print("Gender      :", row[3])
            print("Salary      :", row[4])
            print("DOB         :", row[5])


"""Method to show whole table"""


def show_all():
    cursor.execute("SELECT * FROM employee ORDER BY emp_ID")
    print("***************************************Employee DataBase*******************************")
    print(
        "\nEmployee_ID:                  First_name:                   Last_name:                    Gender:          "
        "             Salary:                       DOB:")
    try:
        for row in cursor.fetchall():
            emp_data = [row[0], row[1], row[2], row[3], str(row[4]), row[5]]
            print(''.join([v.ljust(30, ' ') for v in emp_data]))
    except FileNotFoundError:
        print("No Employee data yet. Please add employees")


def delete_emp(emp_id):
    cursor.execute("""DELETE FROM employee WHERE emp_ID LIKE ?;""", (emp_id,))
    connection.commit()


while True:
    user_input = input("\n1.ADD new employee"
                       "\n2.Delete a employee"
                       "\n3.Search a Employee"
                       "\n4.Show all Employees"
                       "\n5.Quit"
                       "\nEnter choice(1-5)")
    if user_input == '5':
        break
    elif user_input == '1':
        print("Enter Employee details:")
        emp_id = input("Enter employee Id :")
        fname = input("Enter first name :")
        lname = input("Enter last name :")
        gender = input("Enter gender(m/f/o):")
        joining_date = input("Enter Salary(INR) :")
        dob = input("Enter date of birth(yyyy-mm-dd):")
        employee_add(emp_id, fname, lname, gender, joining_date, dob)
        input("\n Press Enter to continue")
    elif user_input == '2':
        delete_emp(input("Enter Employee ID"))
        show_all()
        input("Employee Was removed\nPress Enter to continue")
    elif user_input == '3':
        find_emp_id(input("Enter Employee ID"))
        input("Press ENTER to continue")
    elif user_input == '4':
        show_all()
        input("Press ENTER to continue")
    else:
        print("Wrong input")
