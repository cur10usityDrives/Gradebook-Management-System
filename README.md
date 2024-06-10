# Grade Management System

## Overview

The Grade Management System is a Python-based application designed to streamline the process of managing grades for courses and students. 
It provides a set of classes for defining grading policies, representing student records, handling the serialization/deserialization of 
data to and from JSON files, and an interface for user interaction via the command-line interface (CLI).

## Purpose

The purpose of this project is to offer a flexible and efficient solution for educational institutions, instructors, and administrators to 
manage grading policies and student records. By automating the grading process and providing an organized way to store and retrieve data, 
the Grade Management System aims to save time and reduce errors associated with manual grading and record-keeping.

## Structure

The project consists of the following components:

- **GradePolicy Class**: Defines the grading policy for a course, including the number of assignments, tests, and final exams, as well as their respective weights.
  
- **Student Class**: Represents a student, including their ID, first name, last name, grades for assignments, tests, and final exams, final score, and final grade.
  
- **GradePolicyRepo Class**: Manages the serialization and deserialization of `GradePolicy` objects to and from a JSON file (`gradepolicy.dat`).
  
- **StudentRepo Class**: Manages the serialization and deserialization of `Student` objects to and from a JSON file (`grades.dat`).
  
- **Gradebook Class**: Coordinates the interaction between grading policies, student records, and the user interface, including functionalities
- such as adding students, calculating final scores, computing final grades, and more.
  
- **App Class**: Acts as the interface for users via the command-line interface (CLI), allowing users to interact with the system, view grades, add students, and more.
  
- **UML Diagrams**: The project includes UML diagrams, including class diagrams and use case diagrams, to provide a visual representation of the
- system's architecture and functionality.

## Development Process

The development process for this project follows a systematic approach, including:

1. **Planning**: Identifying requirements, defining features, and outlining the project's architecture.
  
2. **Implementation**: Writing code to implement the defined features, ensuring adherence to best practices and coding standards.
  
3. **Testing**: Performing unit tests, integration tests, and system tests to verify the functionality, reliability, and performance of the application.
  
4. **Documentation**: Creating comprehensive documentation, including README files, code comments, and user guides, to facilitate understanding and usage of the application.

## Instructions for Contributors

Contributions to the Grade Management System are welcome! If you would like to contribute to the project, please follow these guidelines:

1. **Fork the Repository**: Fork the repository to your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/grade-management-system.git
   ```

3. **Create a Branch**: Create a new branch for your contributions:
   ```bash
   git checkout -b feature-name
   ```

4. **Make Changes**: Make your desired changes to the codebase, ensuring adherence to coding standards and best practices.

5. **Commit Changes**: Commit your changes with descriptive commit messages:
   ```bash
   git commit -m "Add feature-name"
   ```

6. **Push Changes**: Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```

7. **Open a Pull Request**: Open a pull request from your forked repository to the main repository.

8. **Review and Merge**: Participate in the review process, address any feedback, and collaborate with the maintainers to merge your changes into the main codebase.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Natnael Haile
