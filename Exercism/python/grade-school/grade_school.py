class School(object):
    """Creates a roster for the school."""
    def __init__(self):
        self.students = list()

    def add_student(self, name: str, grade: list) -> None:
        """Adds a student to the school roster."""
        self.students.append(Student(name, grade))

    def roster(self) -> list:
        """A sorted list of all students in the school."""
        return [s.name for s in sorted(
            self.students,
            key=lambda s: (s.grade, s.name)
        )]

    def grade(self, grade_number: int) -> list:
        """A sorted list of all students in a grade."""
        return sorted([s.name for s in self.students
                       if s.grade == grade_number])


class Student(object):
    """Template for school students"""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
