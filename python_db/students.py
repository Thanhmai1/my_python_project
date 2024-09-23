import mysql.connector
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="t2308m"
    )

mydb = connect_to_db()  
def insert_student(name, age, grade):    
    cursor = mydb.cursor()
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(sql, values)

    mydb.commit()

    print(cursor.rowcount, 'was inserted')
    
def get_all_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    for x in students:
        print(students)
        
def main():
    while True:
        print("----Menu----")
        print('1. Insert students')
        print("2. Display all students")
        print("3. Exit")
        print("Enter your choice: ")
        choice = int(input())
        
        if choice == 1:
            name = input('Enter your name: ')
            age = int(input('Enter your age: '))
            grade = int(input("Enter your grade: "))

            insert_student(name, age, grade)
            
        elif choice == 2:
            get_all_students()

        elif choice == 3:
            print("Exitting...")
            break
        
if __name__ == "__main__":
    main()