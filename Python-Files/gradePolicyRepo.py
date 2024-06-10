import json
from gradePolicy import GradePolicy


class GradePolicyRepo:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename

    def write_policy(self, policy: GradePolicy, semester: str, course_code: str) -> None:
        """
        Save GradePolicy instance to a JSON file.
        
        Args:
            policy (GradePolicy): GradePolicy instance to save.
        """

        data: dict[str, int | float | str] = policy.to_dict()
        data["semester"] = semester
        data["course_code"] = course_code
        
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def read_policy(self) -> tuple[GradePolicy, list[str]]:
        """
        Load GradePolicy instance from a JSON file.
        
        Returns:
            GradePolicy: Loaded GradePolicy instance.
        """
        with open(self.filename, 'r') as file:
            data = json.load(file)
            policy = GradePolicy(
                    num_assignments=data["num_assignments"],
                    num_tests=data["num_tests"],
                    num_finalExams=data["num_finalExams"],
                    assignment_weight=data["assignment_weight"],
                    test_weight=data["test_weight"],
                    finalExam_weight=data["finalExam_weight"]
                )
            
            semester_data = [data["semester"]]
            semester_data.append(data["course_code"])
        
        return (policy, semester_data)


def main():
    # Create some GradePolicy instances
    policy = GradePolicy(3, 2, 1, 0.3, 0.4, 0.3)

    # Create a GradePolicyRepo instance
    repo = GradePolicyRepo("policy.dat")

    # Write policy to JSON file
    repo.write_policy(policy, "Fall", "CS501")
    print("Policy saved to", repo.filename)

    # Read policy from JSON file
    loaded_policy = repo.read_policy()
    print("Policy loaded from", repo.filename)

    # Print loaded policy
    print(f"Policy: {loaded_policy}")




if __name__ == "__main__":
    main()
