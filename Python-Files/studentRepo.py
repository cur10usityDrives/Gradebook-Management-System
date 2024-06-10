import json
from student import Student

class StudentRepo:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename

    def write_students(self, students: list[Student]) -> None:
        self.set_students_to_empty_state()
        """
        Save list of Student instances to a JSON file.
        
        Args:
            students (list): List of Student instances.
            filename (str): Name of the JSON file to save.
        """
        data: list[dict[str, int | str | dict[int, float] | float | None]] = []
        for student in students:
            student_data = {
                "student_id": student.student_id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "assignments": student.assignments,
                "tests": student.tests,
                "final_exams": student.finalExams,
                "final_score": student.final_score,
                "final_grade": student.final_grade
            }
            data.append(student_data)
        
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def read_students(self) -> list[Student]:
        """
        Load list of Student instances from a JSON file.
        
        Args:
            filename (str): Name of the JSON file to load.
        
        Returns:
            list: List of Student instances.
        """
        students: list[Student] = []
        with open(self.filename, 'r') as file:
            data = json.load(file)
            for student_data in data:
                student = Student(
                        student_data["student_id"],
                        student_data["first_name"],
                        student_data["last_name"]
                    )
                for assignment_id, score in student_data["assignments"].items():
                    student.add_assignment(int(assignment_id), score)
                for test_id, score in student_data["tests"].items():
                    student.add_test(int(test_id), score)
                for exam_id, score in student_data["final_exams"].items():
                    student.add_final_exam(int(exam_id), score)
                student.final_score = student_data["final_score"]
                student.final_grade = student_data["final_grade"]
                students.append(student)
        
        return students
    
    def set_students_to_empty_state(self) -> None:
        """Sets the "grades.dat" file to an empty state because a new semester was set up."""
        with open("grades.dat", "w") as file:
            json.dump([], file)


def main():
    # Create some students
    students = [
        Student(1, "John", "Doe"),
        Student(2, "Jane", "Smith")
    ]

    students[0].add_assignment(1, 95)
    students[0].add_test(1, 95)
    students[0].add_final_exam(1, 95)
    students[0].add_assignment(2, 95)
    students[1].add_test(1, 95)
    students[1].add_final_exam(1, 95)
    students[1].add_assignment(2, 95)

    # Save students to JSON file
    repository = StudentRepo("grades.dat")
    repository.write_students(students)
    print("Students saved to", repository.filename)

    # Load students from JSON file
    loaded_students = repository.read_students()
    print("Students loaded from", repository.filename)

    # Print loaded students
    for student in loaded_students:
        print(f"Student ID: {student.student_id}, Name: {student.first_name} {student.last_name}")
        print("Assignments:", student.assignments)
        print("Tests:", student.tests)
        print("Final Exams:", student.finalExams)
        print()


if __name__ == "__main__":
    main()
