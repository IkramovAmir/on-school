from school import students, courses, grades

def main() -> None:
    """
    Main function that drives the On-School system. It displays the main menu,
    handles user registration and login, and provides an interface for enrolled students
    to interact with courses and check grades.
    """
    students_data = {}
    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]
    grades_data = {}

    while True:
        print("\n=== Welcome to On-School ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            # Register a new student
            student_email = input("Enter your email: ")
            student_name = input("Enter your name: ")
            student_password = input("Enter your password: ")
            
            if student_email in students_data:
                print(f"Student with email {student_email} already exists!")
            else:
                students_data[student_email] = {
                    "students_name": student_name,
                    "password": student_password,
                    "enrolled_courses": []
                }
                print(f"Registration successful! Welcome, {student_name}.")

        elif choice == "2":
            # Login process
            student_email = input("Enter your email: ")
            student_password = input("Enter your password: ")
            
            if student_email not in students_data:
                print("Student not found. Please register first.")
                continue
            
            if students_data[student_email]["password"] != student_password:
                print("Incorrect password. Please try again.")
                continue

            print(f"\nLogin successful! Welcome back, {students_data[student_email]['students_name']}.")

            # Main Menu
            while True:
                print(f"\n--- Main Menu for {students_data[student_email]['students_name']} ---")
                print("1. View Available Courses")
                print("2. Enroll in a Course")
                print("3. View My Courses")
                print("4. Check My Grades")
                print("5. Logout")
                
                menu_choice = input("Choose an option: ")

                if menu_choice == "1":
                    # View Available Courses
                    courses.view_courses(courses_data)
                
                elif menu_choice == "2":
                    # Enroll in a Course
                    students.enroll_in_course(courses_data, students_data, student_email)
                
                elif menu_choice == "3":
                    # View My Courses
                    students.view_enrolled_courses(students_data, student_email)
                
                elif menu_choice == "4":
                    # Check My Grades
                    grades.check_grades(grades_data, student_email)
                
                elif menu_choice == "5":
                    # Logout
                    print(f"Goodbye, {students_data[student_email]['students_name']}!")
                    break
                
                else:
                    print("Invalid option. Please try again.")
        
        elif choice == "3":
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()