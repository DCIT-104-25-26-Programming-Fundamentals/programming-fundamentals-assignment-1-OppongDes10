
def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("    STUDENT RECORD SYSTEM MENU")
    print("=" * 40)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    print("=" * 40)


def add_student(students):
    """Add a new student record (list of dictionaries)."""
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return
    

    for student in students:
        if student["id"] == student_id:
            print("Error: Student ID already exists.")
            return
    
    try:
        num_scores = int(input("How many scores? "))
        if num_scores < 1:
            print("Error: Must enter at least 1 score.")
            return
        
        scores = []
        for i in range(1, num_scores + 1):
            score = int(input(f"Enter score {i}: "))
            scores.append(score)

        student = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        students.append(student)
        print(f'Student "{name}" added successfully.')
        
    except ValueError:
        print("Error: Scores must be valid numbers.")


def display_all_students(students):
    """Display all students in a formatted table."""
    if not students:
        print("\nNo students found. The record is empty.")
        return
    
    print("\n" + "-" * 70)
    print(f"{'Name':<18} {'ID':<12} {'Scores':<25} {'Average':<10}")
    print("-" * 70)
    
    for student in students:
        scores_str = ", ".join(map(str, student["scores"]))
        avg = sum(student["scores"]) / len(student["scores"]) if student["scores"] else 0
        print(f"{student['name']:<18} {student['id']:<12} {scores_str:<25} {avg:.2f}")
    
    print("-" * 70)


def calculate_average(students):
    """Calculate and display average score for a specific student by ID."""
    if not students:
        print("Error: No students in the system.")
        return
    
    try:
        student_id = int(input("Enter student ID: "))
        
        for student in students:
            if student["id"] == student_id:
                if not student["scores"]:
                    print(f"{student['name']} has no scores.")
                    return
                avg = sum(student["scores"]) / len(student["scores"])
                print(f"{student['name']}'s average score: {avg:.2f}")
                return
        
        print("Error: Student with that ID not found.")
        
    except ValueError:
        print("Error: Please enter a valid ID number.")


if __name__ == "__main__":
    students = [] 
    print("=== STUDENT RECORD MANAGEMENT SYSTEM STARTED ===\n")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("\nThank you for using the Student Record System. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")