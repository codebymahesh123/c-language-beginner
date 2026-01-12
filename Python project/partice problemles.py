

def proje():
        # Initialize an empty dictionary to store student data
        student_marks = {}

def display_menu():
    """Displays the interactive menu to the user."""
    print("\n--- Student Marks Dictionary Operations ---")
    print("A: Add a student (Name & Marks)")
    print("B: Update marks for an existing student")
    print("C: Search for a student's marks")
    print("D: Display all students and marks")
    print("E: Exit the program")
    print("-" * 40)

def add_student(data):
    """Adds a new student name (key) and marks (value) to the dictionary."""
    name = input("Enter student name to add: ").strip().title()
    if name in data:
        print(f"⚠️ Error: Student '{name}' already exists. Use 'B' to update marks.")
        return

    while True:
        try:
            marks = int(input(f"Enter marks for {name}: "))
            if marks < 0:
                 print("Marks cannot be negative. Please try again.")
                 continue
            data[name] = marks
            print(f"✅ Success: Student '{name}' with marks {marks} added.")
            break
        except ValueError:
            print("❌ Invalid input. Marks must be an integer.")

def update_marks(data):
    """Updates the marks for an existing student."""
    name = input("Enter student name to update marks for: ").strip().title()
    if name not in data:
        print(f"⚠️ Error: Student '{name}' not found.")
        return

    print(f"Current marks for {name}: {data[name]}")
    while True:
        try:
            new_marks = int(input(f"Enter new marks for {name}: "))
            if new_marks < 0:
                 print("Marks cannot be negative. Please try again.")
                 continue
            data[name] = new_marks
            print(f"🔄 Success: Marks for '{name}' updated to {new_marks}.")
            break
        except ValueError:
            print("❌ Invalid input. Marks must be an integer.")

def search_student(data):
    """Searches for a student and displays their marks."""
    name = input("Enter student name to search: ").strip().title()
    if name in data:
        print(f"🔍 Found: The marks for student '{name}' are **{data[name]}**.")
    else:
        print(f"❌ Not Found: Student '{name}' is not in the dictionary.")

def display_all(data):
    """Displays all students and their marks in the dictionary."""
    if not data:
        print("🤷 The dictionary is currently empty.")
        return

    print("\n📚 All Student Records:")
    print("----------------------------")
    # Sort the dictionary by student name (key) for better presentation
    for name, marks in sorted(data.items()):
        print(f"Name: {name:<20} | Marks: {marks}")
    print("----------------------------")

# --- Main Program Loop ---
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (A, B, C, D, E): ").strip().upper()

        if choice == 'A':
            add_student(student_marks)
        elif choice == 'B':
            update_marks(student_marks)
        elif choice == 'C':
            search_student(student_marks)
        elif choice == 'D':
            display_all(student_marks)
        elif choice == 'E':
            print("\n👋 Exiting the program. Goodbye!")
            break
        else:
            print("\n🚨 Invalid choice. Please select A, B, C, D, or E.")
proje()
