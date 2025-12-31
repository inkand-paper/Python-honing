import json
import os

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        # Ensure marks are stored as float for calculation
        self.marks = float(marks)

    def to_dict(self):
        """Converts object to dictionary for JSON storage."""
        return {"name": self.name, "roll": self.roll, "marks": self.marks}

    # --- Task #5 Required Methods ---
    def show_info(self):
        """Prints name & roll."""
        print(f"🎓 Student: {self.name} | Roll: {self.roll}")

    def show_result(self):
        """Checks pass/fail status (Pass >= 45)."""
        status = "PASSED ✅" if self.marks >= 45 else "FAILED ❌"
        print(f"   Result: {status} (Marks: {self.marks})")

    def update_marks(self, extra_marks):
        """Adds marks to the current score."""
        self.marks += float(extra_marks)
        print(f"   🆙 Marks updated for {self.name}! New Score: {self.marks}")
    # -------------------------------

    def __str__(self):
        return f"{self.name.ljust(15)} | {self.roll.ljust(12)} | {self.marks}"

class StudentRecord:
    def __init__(self, filename="student_record.json"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def add_student(self, name, roll, marks):
        new_student = Student(name, roll, marks)
        self.students.append(new_student)
        self.save_to_file()
        print(f"   💾 Saved {name} to file.")

    def find_student(self, name):
        """Helper to find a student object by name."""
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def update_student_marks(self, name, extra_marks):
        """Finds student, updates marks, and saves to JSON."""
        student = self.find_student(name)
        if student:
            student.update_marks(extra_marks)
            self.save_to_file() # <--- Key Step: Save changes to JSON
        else:
            print(f"   Error: '{name}' not found.")

    def show_results_only(self):
        """Uses the show_result method for all students."""
        if not self.students:
            print("\n   Record is empty.")
        else:
            print("\n--- 📊 EXAM RESULTS ---")
            for student in self.students:
                student.show_info()
                student.show_result()
                print("-" * 20)

    def remove_student(self, name):
        student = self.find_student(name)
        if student:
            self.students.remove(student)
            self.save_to_file()
            print(f"\n   🗑️ Removed: {name}")
        else:
            print(f"\n   Error: '{name}' not found")

    def save_to_file(self):
        """Saves the current list of students to a JSON file."""
        with open(self.filename, "w") as f:
            json_data = [s.to_dict() for s in self.students]
            json.dump(json_data, f, indent=4)

    def load_from_file(self):
        """Loads students from JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    # Reconstruct Student objects from dictionaries
                    self.students = [Student(item['name'], item['roll'], item['marks']) for item in data]
            except Exception as e:
                print(f"Error loading file: {e}")
                self.students = []
        else:
            self.students = []

    def show_all(self):
        if not self.students:
            print("\n   The student record book is empty")
        else:
            print("\n" + "="*40)
            print(f"{'NAME'.ljust(15)} | {'ROLL'.ljust(12)} | MARKS")
            print("-" * 40)
            for student in self.students:
                print(student)
            print("="*40)

def main():
    record = StudentRecord()
    
    while True:
        print("\n--- 📱 PERSISTENT STUDENT RECORD (JSON) ---")
        print("1. Add Student")
        print("2. Update Marks (Task #5)")
        print("3. Check Results (Task #5)")
        print("4. Delete Student")
        print("5. Show All")
        print("6. Exit")
        
        choice = input("Select: ")

        if choice == '1':
            record.add_student(input("Name: "), input("Roll: "), input("Marks: "))
        elif choice == '2':
            name = input("Enter Student Name: ")
            marks = input("Add how many marks? ")
            record.update_student_marks(name, marks)
        elif choice == '3':
            record.show_results_only()
        elif choice == '4':
            record.remove_student(input("Name to delete: "))
        elif choice == '5':
            record.show_all()
        elif choice == '6':
            print("👋 Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
