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
    
def get_all_students():    
    cursor.execute("SELECT students.name, ratings.rating FROM students INNER JOIN ratings ON students.grade = ratings.grade")
    students = cursor.fetchall()    
    
    for x in students:
        print(students)

def get_random_students():
    sql = "SELECT name, grade FROM students ORDER BY RAND() LIMIT 1"
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
        print("6. Exit")
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
            print("Exitting...")
            break
        
if __name__ == "__main__":
    main()