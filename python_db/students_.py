import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="t2308m"
    )
    
mydb = connect_to_db()  
cursor = mydb.cursor()

def insert_student(name, grade):    
    sql = "INSERT INTO students (name, grade) VALUES (%s, %s)"
    values = (name, grade)
    cursor.execute(sql, values)

    mydb.commit()

    print(cursor.rowcount, 'was inserted')

def add_subject(name):
    sql = "INSERT INTO subjects (name_subject) VALUES (%s)"    
    values = (name)
    cursor.execute(sql, (values, ))
    
    mydb.commit()
    print(cursor.rowcount, ' was inserted')
    

def add_students_subject(student_id, subject_id):
    sql = "INSERT INTO students_subject (student_id, subject_id) VALUES (%s, %s)"    
    values = (student_id, subject_id)
    cursor.execute(sql, values)
    
    mydb.commit()
    print(cursor.rowcount, ' was inserted')
    
def get_all_students():
    sql = "SELECT students.name, ratings.rating, students_subject.student_id, sub.id AS subject_id, sub.name_subject FROM students INNER JOIN ratings ON students.grade = ratings.grade INNER JOIN students_subject ON students.id = students_subject.student_id INNER JOIN subjects sub ON students_subject.subject_id = sub.id;"
    cursor.execute(sql)
    students = cursor.fetchall()

    for student in students:
        print(student)
    
        
def get_students_by_point(grade):
    sql = "SELECT students.name, students.grade, ratings.rating FROM students INNER JOIN ratings ON students.grade = ratings.grade WHERE students.grade = '%s'"    
    values = (grade)
    cursor.execute(sql, (values, ))
    students = cursor.fetchall()
    for s in students:
        print(s)
    
    
    
def get_random_students():
    sql = "SELECT students.name, ratings.rating, students_subject.student_id, sub.id AS subject_id, sub.name_subject FROM students INNER JOIN ratings ON students.grade = ratings.grade INNER JOIN students_subject ON students.id = students_subject.student_id INNER JOIN subjects sub ON students_subject.subject_id = sub.id ORDER BY RAND() LIMIT 1"    
    cursor.execute(sql)
    students = cursor.fetchone()      
    if students:
        print(students)
    else:
        print("None")
def update_grade_student(name, grade):
    sql = "UPDATE students SET grade = %s WHERE name = %s"
    
    values = (grade, name)
    cursor.execute(sql, values)
    
    mydb.commit()
    print(cursor.rowcount, 'row were updated')

    
def delete_student(name):
    sql = "DELETE FROM students WHERE name = '%s'"
    values = (name)
    cursor.execute(sql, values)
    
    mydb.commit()
    print(cursor.rowcount, 'was inserted')
    
def main():
    while True:
        print("----Menu----")
        print('1. Insert students')
        print("2. Display all students")
        print("3. Display 1 student")
        print("4. Delete student")
        print("5. Update grade student")
        print("6. Display students by point")
        print("7. Add student subject")
        print("8. Add subject")
        print("9. Exit")
        print("Enter your choice: ")
        choice = int(input())
        
        if choice == 1:
            name = input('Enter your name: ')            
            grade = int(input("Enter your grade: "))

            insert_student(name, grade)
            
        elif choice == 2:
            get_all_students()        
        elif choice == 3:
            get_random_students()
        elif choice == 4:
            name = input("Enter name to delete: ")
            delete_student(name)
        elif choice == 5:
            name = input("Enter name to update: ")
            grade = input("Enter grade to update: ")
            update_grade_student(name, grade)
        elif choice == 6:
            grade = int(input("Enter point: "))
            get_students_by_point(grade)
        elif choice == 7:
            students_id = int(input("Enter your id: "))
            subject_id = int(input("Enter id subject: "))
            add_students_subject(students_id, subject_id)
        elif choice == 8:
            subject_name = input("Enter subject's name: ")
            add_subject(subject_name)
        elif choice == 9:
            print("Exitting...")
            break
        
if __name__ == "__main__":
    main()