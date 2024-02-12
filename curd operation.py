# prompt:  Do CRUD operation for students, teacher, principal using OOPs concept my using mysqlconnector.

import pymysql

# Create a connection to the database
conn =pymysql.connect(
  host="127.0.0.1",
  port=3306,
  user="root",
  password="mysql123",
  database="school"
)

# Create a cursor to execute queries
cursor = conn.cursor()

# Create a class for students
class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
    

  def insert_student(self):
    sql = "INSERT INTO students  VALUES (%s, %s, %s,%s)"
    values = (self.name, self.age, self.grade)
    cursor.execute(sql, values)
    conn.commit()

  def update_student(self, id):
    sql = "UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s"
    values = (self.name, self.age, self.grade, id)
    cursor.execute(sql, values)
    conn.commit()

  def delete_student(self, id):
    sql = "DELETE FROM students WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)
    conn.commit()

# Create a class for teachers
class Teacher:
  def __init__(self, name, age, subject):
    self.name = name
    self.age = age
    self.subject = subject

  def insert_teacher(self):
    sql = "INSERT INTO teachers (name, age, subject) VALUES (%s, %s, %s)"
    values = (self.name, self.age, self.subject)
    cursor.execute(sql, values)
    conn.commit()

  def update_teacher(self, id):
    sql = "UPDATE teachers SET name=%s, age=%s, subject=%s WHERE id=%s"
    values = (self.name, self.age, self.subject, id)
    cursor.execute(sql, values)
    conn.commit()

  def delete_teacher(self, id):
    sql = "DELETE FROM teachers WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)
    conn.commit()

# Create a class for principals
class Principal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def insert_principal(self):
    sql = "INSERT INTO principals (name, age) VALUES (%s, %s)"
    values = (self.name, self.age)
    cursor.execute(sql, values)
    conn.commit()

  def update_principal(self, id):
    sql = "UPDATE principals SET name=%s, age=%s WHERE id=%s"
    values = (self.name, self.age, id)
    cursor.execute(sql, values)
    conn.commit()

  def delete_principal(self, id):
    sql = "DELETE FROM principals WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)
    conn.commit()

# Create a function to print the list of students
def print_students():
  sql = "SELECT * FROM students"
  cursor.execute(sql)
  students = cursor.fetchall()
  for student in students:
    print(student)

# Create a function to print the list of teachers
def print_teachers():
  sql = "SELECT * FROM teachers"
  cursor.execute(sql)
  teachers = cursor.fetchall()
  for teacher in teachers:
    print(teacher)

# Create a function to print the list of principals
def print_principals():
  sql = "SELECT * FROM principals"
  cursor.execute(sql)
  principals = cursor.fetchall()
  for principal in principals:
    print(principal)

# Create a function to get the user input
def get_user_input():
  option = input("Enter your option (1-4): ")
  return option

# Create a loop to keep the program running until the user enters 4
while True:
  # Print the menu
  print("Menu:")
  print("1. Insert a student")
  print("2. Update a student")
  print("3. Delete a student")
  print("4. Exit")

  # Get the user input
  option = get_user_input()

  # Perform the selected action
  if option == "1":
    # Create a student object
    student = Student(input("Enter the student's name: "), input("Enter the student's age: "), input("Enter the student's grade: "))

    # Insert the student into the database
    student.insert_student()

  elif option == "2":
    # Get the student's id
    id = input("Enter the student's id: ")

    # Create a student object
    student = Student(input("Enter the student's new name: "), input("Enter the student's new age: "), input("Enter the student's new grade: "))

    # Update the student in the database
    student.update_student(id)

  elif option == "3":
    # Get the student's id
    id = input("Enter the student's id: ")

    # Delete the student from the database
    student = Student(input("Enter the student's new name: "), input("Enter the student's new age: "), input("Enter the student's new grade: "))
  
    # delete the student in the database
    student.delete_student(id)

  elif option == "4":
    # Exit the program
    break

  else:
    # Invalid option
    print("Invalid option.")

# Close the connection to the database
conn.close()