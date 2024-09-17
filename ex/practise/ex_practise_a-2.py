students = [
    {"name": 'Nguyen Van A', "class": 'T2308M', "point 1": 7, "point 2": 6}
]

def add_student():
    name = input("Enter name: ")
    classes = input("Enter class: ")
    diem_1 = float(input("Enter point 1: "))
    diem_2 = float(input("Enter point 2: "))

    student = {
        "name": name,
        "class": classes,
        "point 1": diem_1,
        "point 2": diem_2
    }
    students.append(student)
    print("Student added successfully!")

def calculate_grade(point1, point2):
    final_score = 0.3 * point1 + 0.7 * point2
    
    if final_score < 4.0:
        return 'F'
    elif 4.0 <= final_score < 5.5:
        return 'D'
    elif 5.5 <= final_score < 6.5:
        return 'C'
    elif 6.5 <= final_score < 8.5:
        return 'B'
    else:
        return 'A'

def display_students():
    if students:
        print("TT  Name            Class   Point 1  Point 2  Final Grade")
        for stt, student in enumerate(students, start=1):
            name = student['name']
            classes = student['class']
            point1 = student['point 1']
            point2 = student['point 2']
            grade = calculate_grade(point1, point2)
            
            print(f"{stt:<3} {name:<15} {classes:<7} {point1:<8} {point2:<8} {grade}")
    else:
        print("Don't have any students.")

def grade_sort():
    sorted_students = sorted(students, key=lambda s: 0.3 * s['point 1'] + 0.7 * s['point 2'], reverse=True)
    print("Students sorted by final grade:")
    print("TT  Name            Class   Point 1  Point 2  Final Grade")
    for stt, student in enumerate(sorted_students, start=1):
        name = student['name']
        classes = student['class']
        point1 = student['point 1']
        point2 = student['point 2']
        grade = calculate_grade(point1, point2)
        
        print(f"{stt:<3} {name:<15} {classes:<7} {point1:<8} {point2:<8} {grade}")

def main():
    while True:
        print("------- Menu -------")
        print("1. Create students")
        print("2. Display all students")
        print("3. Display students sorted by final grade")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            grade_sort()
        else:
            break
        
main()
