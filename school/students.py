def register_student(students_data: dict[str, dict[str, str]]) -> None:
    """
    Registers a new student by collecting their name, email, and password, 
    and stores the information in the students_data dictionary.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.
    """    
    email = input("Input your email: ")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    
    # Save the student's information
    students_data[email] = {"students_name": name, "students_pass": password, "enrolled_courses": []}


def login_student(students_data: dict[str, dict[str, str]]) -> str | None:
    """
    Allows a student to log in by entering their email and password. 
    If the login is successful, it returns the student's email.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.

    Returns:
        str: The student's email if login is successful, else None.
    """
    email = input("Email address: ")
    password = input("Password: ")

    # Check if email exists and password matches
    if email in students_data:
        if students_data[email]["students_pass"] == password:
            return email  # Returning email instead of student's name for login success
    print("Login failed. Invalid email or password.")
    return None


def enroll_in_course(courses_data: list[dict[str, str]], students_data: dict[str, dict[str, str]], student_email: str) -> None:
    """
    Enroll a student in a selected course.

    Args:
        courses_data (list): List of available courses.
        students_data (dict): A dictionary of student details.
        student_email (str): The email of the student to enroll.
    """
    # Display available courses
    print("\nAvailable Courses:")
    for index, course in enumerate(courses_data, start=1):
        print(f"{index}. {course['course_name']} - Instructor: {course['instructor']}, Duration: {course['duration']} hours")
    
    course_number = int(input("\nSelect the course number to enroll in: ")) - 1
    if 0 <= course_number < len(courses_data):
        course = courses_data[course_number]
        students_data[student_email]["enrolled_courses"].append(course)
        print(f"Successfully enrolled in {course['course_name']}!")
    else:
        print("Invalid course selection.")


def view_enrolled_courses(students_data: dict[str, dict[str, list[str]]], student_email: str) -> None:
    """
    Displays the list of courses that the student has enrolled in.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (including enrolled courses) are stored as values.
        student_email (str): The email of the student whose enrolled courses are being displayed.
    """
    if student_email in students_data:
        enrolled_courses = students_data[student_email].get("enrolled_courses", [])
        if enrolled_courses:
            print("\nYour Enrolled Courses:")
            for index, course in enumerate(enrolled_courses, start=1):
                print(f"{index}. {course['course_name']} - Instructor: {course['instructor']}, Duration: {course['duration']} hours")
        else:
            print("You haven't enrolled in any courses yet.")
    else:
        print("Student not found.")