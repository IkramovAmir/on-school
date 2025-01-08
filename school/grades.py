def check_grades(grades_data, student_email):
    """
    Display grades for a student.
    """
    print("\nMy Grades:")
    enrolled_courses = grades_data.get(student_email, {})
    
    if not enrolled_courses:
        print("No grades available. You are either not enrolled in any courses or grades are not yet assigned.")
    else:
        for course, grade in enrolled_courses.items():
            print(f"{course}: {grade}")