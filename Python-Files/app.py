from __future__ import annotations
from typing import Callable
from gradebook import Gradebook
from gradePolicy import GradePolicy
from student import Student


class App:
    def __init__(self) -> None:
        self.__gradebook = Gradebook()

    @property
    def gradebook(self) -> Gradebook:
        return self.__gradebook
    
    def show_title(self) -> None:
        print(self.__gradebook)

    def setup_new_semester(self) -> None:
        """Set up for the new semester."""
        if self.gradebook.policy:
            conf = input("Are you sure you want to set a new semester(y/n)? ").lower()
            if conf == "y":
                self.gradebook.initialize_grades_to_empty_state()
                self.gradebook.semester = input("Enter semester name(fall/spring/summer): ").capitalize()
                self.gradebook.course_code = input("Enter course code(CS500/CS545): ").upper()
                num_assignments = int(input("Enter the number of programming assignments (0-6): "))
                while not (0 <= num_assignments <= 6):
                    print("Invalid input. 😞 Number of assignments should be 0-6.")
                    num_assignments = int(input("Enter the number of programming assignments (0-6): "))
                num_tests = int(input("Enter the number of tests (0-4): "))
                while not (0 <= num_tests <= 4):
                    print("Invalid input. 😞 Number of tests should be 0-4.")
                    num_tests = int(input("Enter the number of tests (0-4): "))
                num_final_exams = int(input("Enter the number of final exams (0-1): "))
                while not (0 <= num_final_exams <= 1):
                    print("Invalid input. 😞 Number of final exams should be 0-1.")
                    num_final_exams = int(input("Enter the number of final exams (0-1): "))
                if num_assignments != 0:
                    assignment_weight = float(input("Enter the weight of assignments (0-100%): "))
                    while not (0 <= assignment_weight <= 100):
                        print("Invalid input. 😞 Assignment weights should be 0-100%.")
                        assignment_weight = float(input("Enter the weight of assignments (0-100%): "))
                else:
                    assignment_weight = 0
                if num_tests != 0:
                    test_weight = float(input("Enter the weight of tests (0-100%): "))
                    while not (0 <= test_weight <= 100):
                        print("Invalid input. 😞 Test weights should be 0-100%.")
                        test_weight = float(input("Enter the weight of tests (0-100%): "))
                else:
                    test_weight = 0
                if num_final_exams != 0:
                    final_exam_weight = float(input("Enter the weight of final exam (0-100%): "))
                    while not (0 <= final_exam_weight <= 100):
                        print("Invalid input. 😞 Final exam weights should be 0-100%.")
                        final_exam_weight = float(input("Enter the weight of final exam (0-100%): "))
                else:
                    final_exam_weight = 0
                while not ((assignment_weight + test_weight + final_exam_weight) == 100):
                    print("Invalid input. 😞 Assessment weights should add to a 100%.")
                    if num_assignments != 0:
                        assignment_weight = float(input("Enter the weight of assignments (0-100%): "))
                        while not (0 <= assignment_weight <= 100):
                            print("Invalid input. 😞 Assignment weights should be 0-100%.")
                            assignment_weight = float(input("Enter the weight of assignments (0-100%): "))
                    else:
                        assignment_weight = 0
                    if num_tests != 0:
                        test_weight = float(input("Enter the weight of tests (0-100%): "))
                        while not (0 <= test_weight <= 100):
                            print("Invalid input. 😞 Test weights should be 0-100%.")
                            test_weight = float(input("Enter the weight of tests (0-100%): "))
                    else:
                        test_weight = 0
                    if num_final_exams != 0:
                        final_exam_weight = float(input("Enter the weight of final exam (0-100%): "))
                        while not (0 <= final_exam_weight <= 100):
                            print("Invalid input. 😞 Final exam weights should be 0-100%.")
                            final_exam_weight = float(input("Enter the weight of final exam (0-100%): "))
                    else:
                        final_exam_weight = 0

                grade_policy = GradePolicy(num_assignments, num_tests, num_final_exams,
                                            assignment_weight/100, test_weight/100, final_exam_weight/100)
                self.gradebook.policy = grade_policy
                self.gradebook.save_policy_to_db()
                if self.gradebook.policy:
                    print("Semester successfully set up. 🤩")
            else:
                return None

    def add_student(self) -> None:
        """Add a student."""
        student_id = int(input("Enter student ID (1-9999): "))
        while not (1 <= student_id <= 9999):
            print("Invalid input. 😞 Student ID should be 1-9999.")
            student_id = int(input("Enter student ID (1-9999): "))
        first_name = input("Enter student's first name: ")
        while not (0 < len(first_name) <= 20):
            print("Invalid input. 😞 Student first name should neither be empty nor more than 20 characters.")
            first_name = input("Enter student's first name (no more than 20 characters): ")
        last_name = input("Enter student's last name: ")
        while not (0 < len(last_name) <= 20):
            print("Invalid input. 😞 Student first name should neither be empty nor more than 20 characters.")
            last_name = input("Enter student's last name (no more than 20 characters): ")
        student = Student(student_id, first_name.capitalize(), last_name.capitalize())
        self.gradebook.add_student(student)

    def record_assessment_grade(self, choice: str) -> None:
        """Record grades for assignments, tests, or finals"""

        assessment_type = {'P': 'programming assignment', 'T': 'test', 'F': 'final exam'}[choice]

        self.gradebook.get_policy_from_db()
        policy = self.gradebook.policy
        if policy:
            # Check if the weight of the assessment type is zero
            if (choice == 'P' and policy.assignment_weight == 0) or \
            (choice == 'T' and policy.test_weight == 0) or \
            (choice == 'F' and policy.finalExam_weight == 0):
                print(f"The weight for {assessment_type} is set to 0. Skipping grade recording.")
                return
            
            # Check if the number of assessments recorded is not greater than the number saved in the policy
            num_recorded_assessments = len(self.gradebook.students[0].assignments) if choice == 'P' \
                                    else len(self.gradebook.students[0].tests) if choice == 'T' \
                                    else len(self.gradebook.students[0].finalExams)
            
            num_policy_assessments = policy.num_assignments if choice == 'P' \
                                    else policy.num_tests if choice == 'T' \
                                    else policy.num_finalExams

            if num_recorded_assessments >= num_policy_assessments:
                print(f"The maximum number of {assessment_type}s ({num_policy_assessments}) has already been recorded.")
                return

            # Get the assessment details from the user
            assessment_number = input(f"Enter the {assessment_type} number: ")
            while not assessment_number.isdigit() or int(assessment_number) < 1:
                print(f"Invalid input. 😞 Please enter a positive integer for the {assessment_type} number.")
                assessment_number = input(f"Enter the {assessment_type} number: ")

            # Record grades for each student
            check = True # a bool to check if the assessments were successfully recorded for each student
            self.gradebook.get_students_from_db()
            for student in self.gradebook.students:
                grade = input(f"Enter the grade for {assessment_type} for {student.first_name} {student.last_name} (Student ID: {student.student_id}) (0-100): ")
                while not grade.isdigit() or not 0 <= float(grade) <= 100:
                    print("Invalid input. 😞 Please enter a number between 0 and 100 in % for the grade.")
                    grade = input(f"Enter the grade for {assessment_type} for {student.first_name} {student.last_name} (Student ID: {student.student_id} (0-100)): ")

                # Store the grade based on the assessment type
                if choice == 'P':
                    student.add_assignment(int(assessment_number), float(grade))
                elif choice == 'T':
                    student.add_test(int(assessment_number), float(grade))
                elif choice == 'F':
                    student.add_final_exam(int(assessment_number), float(grade))

                # Check if the assessment grade was successfully recorded for the student
                if choice == 'P' and not student.assignments.get(int(assessment_number)):
                    check = False
                elif choice == 'T' and not student.tests.get(int(assessment_number)):
                    check = False
                elif choice == 'F' and not student.finalExams.get(int(assessment_number)):
                    check = False

            if check:
                self.gradebook.save_students_to_db()
                print(f"Grades for {assessment_type} with assessment number {assessment_number} recorded for all students.🤩")
            else:
                print("Something went wrong! 😞 Please try again.")

    def change_grade(self) -> None:
        """Change a grade for a particular student."""

        # Prompt user for student ID
        student_id = input("Enter the student ID: ")
        while not student_id.isdigit() or int(student_id) not in [student.student_id for student in self.gradebook.students]:
            print("Invalid student ID. 😞 Please enter a valid student ID.")
            student_id = input("Enter the student ID: ")

        # Prompt user for the type of grade to change
        grade_type = input("Enter the type of grade to change (P for programming, T for test, F for final exam): ").upper()
        while grade_type not in ['P', 'T', 'F']:
            print("Invalid grade type. 😞 Please enter P, T, or F.")
            grade_type = input("Enter the type of grade to change (P for programming, T for test, F for final exam): ").upper()

        # Prompt user for the assessment number
        assessment_number = input("Enter the assessment number: ")
        while not assessment_number.isdigit() or int(assessment_number) < 1:
            print("Invalid assessment number. 😞 Please enter a positive integer.")
            assessment_number = input("Enter the assessment number: ")

        # Prompt user for the new grade
        new_grade = input("Enter the new grade: ")
        while not new_grade.isdigit() or not 0 <= int(new_grade) <= 100:
            print("Invalid grade. 😞 Please enter a number between 0 and 100.")
            new_grade = input("Enter the new grade: ")

        # Find the student object
        student = None
        for s in self.gradebook.students:
            if s.student_id == int(student_id):
                student = s
                break

        # Change the grade based on the grade type
        check = False  # a bool to check if the desired modifications were successfully implemented
        if student and self.gradebook.policy:
            if grade_type == 'P' and self.gradebook.policy.num_assignments != 0:
                try:
                    student.add_assignment(int(assessment_number), float(new_grade))
                    if student.assignments.get(int(assessment_number)) == float(new_grade):
                        print(f"Grade for programming assignment {assessment_number} changed for student {student.first_name} {student.last_name}. 🤩")
                        check = True
                except ValueError as e:
                    print(e)
            elif grade_type == 'T' and self.gradebook.policy.num_tests != 0:
                try:
                    student.add_test(int(assessment_number), float(new_grade))
                    if student.tests.get(int(assessment_number)) == float(new_grade):
                        print(f"Grade for test {assessment_number} changed for student {student.first_name} {student.last_name}. 🤩")
                        check = True
                except ValueError as e:
                    print(e)
            elif grade_type == 'F' and self.gradebook.policy.num_finalExams != 0:
                try:
                    student.add_final_exam(int(assessment_number), float(new_grade))
                    if student.finalExams.get(int(assessment_number)) == float(new_grade):
                        print(f"Grade for final exam {assessment_number} changed for student {student.first_name} {student.last_name}. 🤩")
                        check = True
                except ValueError as e:
                    print(e)

            if check:
                self.gradebook.save_students_to_db()

        
    def calculate_final_scores(self) -> None:
        """Calculate final scores for all students."""
        self.gradebook.get_policy_from_db()
        self.gradebook.get_students_from_db()
        self.gradebook.calculate_final_scores()
        self.gradebook.compute_final_grade()
        print("Final scores and grades calculated for all students. 🤩")

    def output_grades(self, order: str) -> None:
        """Output grade data ordered by name or ID."""
        
        # Order students by name or ID
        if order == 'name':
            ordered_students = self.order_students_by_name()
        else:
            ordered_students = self.order_students_by_id()

        # Print grade data for each student
        print("\n######### STUDENT SCORES #########\n")
        for student in ordered_students:
            print(f"{student}")
            print(f"Programming Assignments: {self.display_scores(student.assignments)}")
            print(f"Tests: {self.display_scores(student.tests)}")
            print(f"Final Exam: {self.display_scores(student.finalExams)}")
            print(f"Final Score: {student.final_score}%")
            print(f"Final Grade: {student.final_grade}")
            print("\n####################################\n")
        
    def display_scores(self, scores: dict[int, float]) -> str:
        output = ""
        for k, v in scores.items():
            if output:
                output += ", "
            output += f"{k}: {v}"
        return output
    
    def order_students_by_name(self) -> list[Student]:
        """Order students by name."""
        students_by_name = list(self.gradebook.students)
        students_by_name = self.custom_sort(students_by_name, self.get_last_name)
        return students_by_name

    def order_students_by_id(self) -> list[Student]:
        """Order students by ID."""
        students_by_id = list(self.gradebook.students)
        students_by_id = self.custom_sort(students_by_id, self.get_student_id)
        return students_by_id

    def custom_sort(self, students: list[Student], key_func: Callable[[Student], int | str]) -> list[Student]:
        """Custom sorting algorithm."""
        n = len(students)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key_func(students[j]) > key_func(students[j + 1]): # type: ignore
                    students[j], students[j + 1] = students[j + 1], students[j]
        return students

    def get_last_name(self, student: Student) -> str:
        """Helper function to get last name for sorting."""
        return student.last_name

    def get_student_id(self, student: Student) -> int:
        """Helper function to get student ID for sorting."""
        return student.student_id

    def display_menu(self) -> None:
        """Display the menu."""
        print("\n######### MENU #########\n")
        print("(S) Set up for the new semester")
        print("(A) Add a student")
        print("(P) Record programming assignment score for all students")
        print("(T) Record test score for all students")
        print("(F) Record final exam score for all students")
        print("(C) Change a grade for a particular student")
        print("(G) Calculate final score for all students")
        print("(O) Output the grade data")
        print("(Q) Quit")
        print("\n########################\n")

    def run(self) -> None:
        """Run the application."""
        while True:
            try:
                self.gradebook.get_policy_from_db()
                self.gradebook.get_students_from_db()
                if self.gradebook.policy:
                    print("\n##### CURRENT SEMESTER #####\n")
                    self.show_title()
            except Exception as e:
                print(f"Unexpected error occurred: {e}")
            self.display_menu()
            choice = input("Enter your choice: ").upper()
            if choice == "S":
                self.setup_new_semester()
            elif choice == "A":
                if not self.gradebook.policy:
                    print("Please set up the semester first.")
                    continue
                self.add_student()
            elif choice in ['P', 'T', 'F']:
                if not self.gradebook.policy:
                    print("Please set up the semester first.")
                    continue
                self.record_assessment_grade(choice)
            elif choice == 'C':
                if not self.gradebook.policy:
                    print("Please set up the semester first.")
                    continue
                self.change_grade()
            elif choice == 'G':
                # Check if grading policy is set up
                if not self.gradebook.policy:
                    print("Please set up the semester first.")
                    continue
                self.calculate_final_scores()
            elif choice == 'O':
                # Check if grading policy is set up
                if not self.gradebook.policy:
                    print("Please set up the semester first.")
                    continue
                # Output grade data
                order: str = input("Order by (name/id): ").lower()
                while order not in ['name', 'id']:
                    print("Invalid input. 😞 Please enter a either 'name' or 'id' for the ordering.")
                    order: str = input("Order by (name/id): ").lower()
                self.output_grades(order)
            elif choice == 'Q':
                # Quit and save data
                print("Exiting system.\nBye 👋")
                break
            else:
                print("Invalid choice. 😞 Please try again.")


if __name__ == "__main__":
    app = App()
    app.run()
