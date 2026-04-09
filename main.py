import sqlite3

def create_table():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()
    
def add_students(name,age,grade):
    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    """, (name, age, grade))
    conn.commit()
    conn.close()
    
def view_students():
    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows= cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
        
def menu():
    while True:
        print("\n1. Add a student")
        print("2. View student")
        print("3. Update a student")
        print("4. Delete a student")
        print("5. Exit")
        
        choice = input("Enter a number:")
        
        if choice =="1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_students(name, age, grade)
            
        elif choice == "2":
            view_students()
            
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(student_id, name, age, grade)
            
        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            delete_student(student_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")  
            
def update_student(student_id, name, age, grade):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, grade = ?
        WHERE id = ?
    """, (name, age, grade, student_id))
    conn.commit()
    conn.close()
    print("Student updated.")  
def delete_student(student_id):
    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()           
            
    
create_table()  
menu()
   
