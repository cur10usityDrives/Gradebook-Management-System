class GradePolicy:
    def __init__(self, num_assignments: int, num_tests: int, num_finalExams: int,
                 assignment_weight: float, test_weight: float, finalExam_weight: float) -> None:
        self.__num_assignments = num_assignments
        self.__num_tests = num_tests
        self.__num_finalExams = num_finalExams
        self.__assignment_weight = assignment_weight
        self.__test_weight = test_weight
        self.__finalExam_weight = finalExam_weight

    @property
    def num_assignments(self) -> int:
        return self.__num_assignments

    @property
    def num_tests(self) -> int:
        return self.__num_tests

    @property
    def num_finalExams(self) -> int:
        return self.__num_finalExams

    @property
    def assignment_weight(self) -> float:
        return self.__assignment_weight

    @property
    def test_weight(self) -> float:
        return self.__test_weight

    @property
    def finalExam_weight(self) -> float:
        return self.__finalExam_weight

    def to_dict(self) -> dict[str, int | float | str]:
        return {
            "num_assignments": self.num_assignments,
            "num_tests": self.num_tests,
            "num_finalExams": self.num_finalExams,
            "assignment_weight": self.assignment_weight,
            "test_weight": self.test_weight,
            "finalExam_weight": self.finalExam_weight
        }
    
    def __str__(self) -> str:
        output = "Grade Policy Details:\n"
        output += f"  Assignments: {self.num_assignments} (Weight: {self.assignment_weight * 100}%)\n"
        output += f"  Tests: {self.num_tests} (Weight: {self.test_weight * 100}%)\n"
        output += f"  Final Exams: {self.num_finalExams} (Weight: {self.finalExam_weight * 100}%)"
        return output
    
    def __eq__(self, __other: object):
        if not isinstance(__other, GradePolicy):
            return False
        return (self.__num_assignments == __other.__num_assignments and
                self.__num_tests == __other.__num_tests and
                self.__num_finalExams == __other.__num_finalExams and
                self.__assignment_weight == __other.__assignment_weight and
                self.__test_weight == __other.__test_weight and
                self.__finalExam_weight == __other.__finalExam_weight)
    
    def display(self) -> None:
        print(self)


def main():
    # Create a GradePolicy instance
    grade_policy = GradePolicy(
        num_assignments=3,
        num_tests=2,
        num_finalExams=1,
        assignment_weight=0.3,
        test_weight=0.4,
        finalExam_weight=0.3
    )

    # Access properties
    print("Number of assignments:", grade_policy.num_assignments)
    print("Number of tests:", grade_policy.num_tests)
    print("Number of final exams:", grade_policy.num_finalExams)
    print("Assignment weight:", grade_policy.assignment_weight)
    print("Test weight:", grade_policy.test_weight)
    print("Final exam weight:", grade_policy.finalExam_weight)

    # Convert to dictionary
    policy_dict = grade_policy.to_dict()
    print("Grade policy as dictionary:", policy_dict)
    print(grade_policy)


if __name__ == "__main__":
    main()
