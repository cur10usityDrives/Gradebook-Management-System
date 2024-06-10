from typing import Optional


class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str) -> None:
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__assignments: dict[int, float] = {}
        self.__tests: dict[int, float] = {}
        self.__finalExams: dict[int, float] = {}
        self.__final_score: Optional[float] = None
        self.__final_grade: Optional[str] = None
        # self.__grades: dict[str, int] = {}

    def __str__(self) -> str:
        return f"Student Id :{self.student_id}, Name: {self.first_name} {self.last_name}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Student):
            return self.__student_id == __value.student_id
        else:
            return False

    @property
    def student_id(self) -> int:
        return self.__student_id

    @student_id.setter
    def student_id(self, value: int) -> None:
        if value > 0:
            self.__student_id = value
        else:
            raise ValueError("Student ID must be a positive integer")

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        if value:
            self.__first_name = value
        else:
            raise ValueError("First name must be a non-empty string")

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        if value:
            self.__last_name = value
        else:
            raise ValueError("Last name must be a non-empty string")

    @property
    def assignments(self) -> dict[int, float]:
        return self.__assignments.copy()

    @property
    def tests(self) -> dict[int, float]:
        return self.__tests.copy()

    @property
    def finalExams(self) -> dict[int, float]:
        return self.__finalExams.copy()
    
    @property
    def final_score(self) -> Optional[float]:
        return self.__final_score
    
    @final_score.setter
    def final_score(self, score: float) -> None:
        if score and 0 <= score <= 100:
            self.__final_score = score

    @property
    def final_grade(self) -> Optional[str]:
        return self.__final_grade
    
    @final_grade.setter
    def final_grade(self, grade: str) -> None:
        if grade and len(grade) == 1:
            self.__final_grade = grade.upper()

    def add_assignment(self, assignment_id: int, score: float) -> None:
        if 0 <= score <= 100:
            self.__assignments[assignment_id] = score
        else:
            raise ValueError("Score must be between 0 and 100")

    def remove_assignment(self, assignment_id: int) -> None:
        if assignment_id in self.__assignments:
            del self.__assignments[assignment_id]
        else:
            raise ValueError("No assignment exists with the specified ID")

    def add_test(self, test_id: int, score: float) -> None:
        if score and 0 <= score <= 100:
            self.__tests[test_id] = score
        else:
            raise ValueError("Score must be between 0 and 100")

    def remove_test(self, test_id: int) -> None:
        if test_id in self.__tests:
            del self.__tests[test_id]
        else:
            raise ValueError("No test exists with the specified ID")

    def add_final_exam(self, exam_id: int, score: float) -> None:
        if 0 <= score <= 100:
            self.__finalExams[exam_id] = score
        else:
            raise ValueError("Score must be between 0 and 100")

    def remove_final_exam(self, exam_id: int) -> None:
        if exam_id in self.__finalExams:
            del self.__finalExams[exam_id]
        else:
            raise ValueError("No final exam exists with the specified ID")
        
    def display(self) -> None:
        print(self)


# Example Usage
def main() -> None:
    student = Student(1, "John", "Doe")
    student.first_name = "Jane"  # Setter will update the name
    print(student.first_name)  # Getter will retrieve the name
    student.add_test(5, 95)
    print(student.tests)  # Showing all grades
    print(student)
    

if __name__ == "__main__":
    main()
