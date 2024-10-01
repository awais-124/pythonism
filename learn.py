import os
# Sample Data Storage
students = []

# Helper Functions
def get_student_data():
    """
    Collects and returns a dictionary with valid student information.
    """
    print("ENTER PERSONAL INFORMATION")
    name = input("Enter Student Name: ").strip()
    reg_no = input("Enter Registration Number: ").strip().upper()
    dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
    cgpa = input("Enter CGPA: ").strip()
    semester = input("Enter Semester: ").strip()
    program = input("Enter Program: ").strip()
    father_name = input("Enter Father's Name: ").strip()
    contact = input("Enter Contact Number: ").strip()

    courses = []
    num_courses = int(input("Enter number of courses enrolled: "))
    index = 0
    for _ in range(num_courses):
        print("\n\nENTER DATA FOR COURSE(",index+1,") : ")
        course = {
            "name": input("Enter Course Name: ").strip(),
            "courseCode": input("Enter Course Code: ").strip().upper(),
            "creditHours": input("Enter Credit Hours: ").strip(),
            "teacher": input("Enter Teacher Name: ").strip()
        }
        courses.append(course)

    return {
        "name": name,
        "reg_no": reg_no,
        "dob": dob,
        "cgpa": cgpa,
        "semester": semester,
        "program": program,
        "father_name": father_name,
        "contact": contact,
        "courses": courses
    }

def find_student(reg_no):
    """
    Finds a student by registration number.
    """
    for student in students:
        if student["reg_no"] == reg_no:
            return student
    return None

# Student Functions
def add_student():
    """
    Adds a new student to the system.
    """
    student = get_student_data()
    students.append(student)
    print(f"Student {student['name']} added successfully.")

def remove_student():
    """
    Removes a student from the system by registration number.
    """
    reg_no = input("Enter Registration Number of student to remove: ").strip().upper()
    student = find_student(reg_no)
    
    if student:
        students.remove(student)
        print(f"Student {student['name']} removed successfully.")
    else:
        print(f"No student found with registration number {reg_no}.")

def modify_student():
    """
    Modifies student details.
    """
    reg_no = input("Enter Registration Number of student to modify: ").strip().upper()
    student = find_student(reg_no)
    
    if student:
        print(f"Modifying record for {student['name']}.")
        updated_data = get_student_data()
        student.update(updated_data)  # Update student information
        print(f"Student {student['name']}'s record updated successfully.")
    else:
        print(f"No student found with registration number {reg_no}.")

def display_students():
    """
    Displays all student records in a formatted manner.
    """
    if not students:
        print("No student records available.")
        return

    for student in students:
        print(f"\n=== Student: {student['name']} ===")
        print(f"Registration Number: {student['reg_no']}")
        print(f"Date of Birth: {student['dob']}")
        print(f"CGPA: {student['cgpa']}")
        print(f"Semester: {student['semester']}")
        print(f"Program: {student['program']}")
        print(f"Father's Name: {student['father_name']}")
        print(f"Contact: {student['contact']}")
        print("Courses Enrolled:")
        for course in student['courses']:
            print(f"- {course['name']} (Code: {course['courseCode']}, Credit Hours: {course['creditHours']}, Teacher: {course['teacher']})")
        print("==============================")

def exit_program():
    """
    Exits the program.
    """
    print("Exiting the program.")
    exit()

# Main Function
def main():
    os.system("cls")
    while True:
        print("WELCOME TO PYTHON PROJECT")
        print("STUDENT INFORMATION MANAGEMENT SYSTEM")
        print("MENU - ENTER THE RESPECTIVE NUMBER FOR OPTIONS BELOW")
        print("===================================")
        print("1. ADD STUDENT RECORD")
        print("2. REMOVE STUDENT RECORD")
        print("3. MODIFY STUDENT RECORD")
        print("4. DISPLAY STUDENT RECORDS")
        print("5. EXIT")
        print("===================================")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            modify_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            exit_program()
        else:
            os.system("cls")        
            print("\n\nSELECT A VALID OPTION FROM THE GIVEN MENU.................................\n\n")

if __name__ == "__main__":    
    main()
