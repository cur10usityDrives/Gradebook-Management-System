from typing import Optional
from student import Student
from gradePolicy import GradePolicy
from studentRepo import StudentRepo
from gradePolicyRepo import GradePolicyRepo


class Gradebook:
    def __init__(self) -> None:
        self.__semester: Optional[str] = None
        self.__course_code: Optional[str] = None
        self.__students: list[Student] = []
        self.__policy: Optional[GradePolicy] = None

    def __str__(self) -> str:
        return f"Semester={self.__semester}, Course Code={self.__course_code}"

    @property
    def semester(self) -> Optional[str]:
        return self.__semester
    
    @semester.setter
    def semester(self, semester_name: str) -> None:
        self.__semester = semester_name
    
    @property
    def course_code(self) -> Optional[str]:
        return self.__course_code
    
    @course_code.setter
    def course_code(self, code: str) -> None:
        self.__course_code = code
    
    @property
    def students(self) -> list[Student]:
        return self.__students
    
    @property
    def policy(self) -> Optional[GradePolicy]:
        return self.__policy

    @policy.setter
    def policy(self, policy: GradePolicy) -> None:
        self.__policy = policy

    def get_students_from_db(self) -> None:
        repo = StudentRepo("grades.dat")
        self.__students = repo.read_students()

    def get_policy_from_db(self) -> None:
        repo = GradePolicyRepo("policy.dat")
        data = repo.read_policy()
        self.__policy = data[0]
        self.__semester = data[1][0]
        self.__course_code = data[1][1]

    def save_students_to_db(self) -> None:
        repo = StudentRepo("grades.dat")
        repo.write_students(self.__students)

    def save_policy_to_db(self) -> None:
        if self.__policy and self.__semester and self.__course_code:
            repo = GradePolicyRepo("policy.dat")
            repo.write_policy(self.__policy, self.__semester, self.__course_code)

    def add_student(self, student: Student) -> None:
        if self.__students:
            self.save_policy_to_db()
        self.get_students_from_db()
        if student not in self.__students:
            self.__students.append(student)
            self.save_students_to_db()
            print("Student successfully added. 🤩")
        else: 
            print("Student already in Gradebook! 😞")

    def initialize_grades_to_empty_state(self) -> None:
        """sets the grades.dat to an empty state because a new semester was set up."""
        repo = StudentRepo("grades.dat")
        repo.set_students_to_empty_state()

    def calculate_final_scores(self) -> None:
        """Calculate final scores for all students."""
        self.get_students_from_db()
        self.get_policy_from_db()

        if self.__policy and self.__students:
            for student in self.__students:
                total_assignment_score = self.total_score(student.assignments) if self.__policy.num_assignments != 0 else 0
                total_test_score = self.total_score(student.tests) if self.__policy.num_tests != 0 else 0
                total_final_exam_score = self.total_score(student.finalExams) if self.__policy.num_finalExams != 0 else 0

                # Calculate percentage and final score considering only the non-zero weights
                assignment_percentage = ((total_assignment_score / self.__policy.num_assignments) * self.__policy.assignment_weight) if self.__policy.assignment_weight != 0 else 0
                test_percentage = ((total_test_score / self.__policy.num_tests) * self.__policy.test_weight) if self.__policy.num_tests != 0 else 0
                final_exam_percentage = ((total_final_exam_score / self.__policy.num_finalExams) * self.__policy.finalExam_weight) if self.__policy.finalExam_weight != 0 else 0

                # Calculate final score
                final_score = round(assignment_percentage + test_percentage + final_exam_percentage, 2)
                # Store the final score in the student's record
                student.final_score = final_score

            # Save the updated student records to the database
            self.save_students_to_db()

    def total_score(self, scores: dict[int, float]) -> float:
        """Calculate the total score for a particular assessment type."""
        total_score = 0
        for score in scores.values():
            total_score += score
        return total_score
    
    def compute_final_grade(self) -> None:
        """Compute the final grade letter based on final scores for all students."""
        self.get_students_from_db()
        grade_policy = {"A": 90, "B": 80, "C": 75, "D": 60, "F": 0}
        # A bool to check if the final scores of all students are already calculated and they exist in the repository
        check = True
        if self.__students:
            for student in self.__students:
                if student.final_score:
                    # Find the appropriate letter grade based on the final score
                    for grade in sorted(grade_policy.keys(), reverse=False):
                        threshold = grade_policy[grade]
                        if student.final_score >= threshold:
                            student.final_grade = grade.upper()
                            break
                else:
                    check = False
        if check:
            self.save_students_to_db()
