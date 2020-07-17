
class Cohort:
    def __init__(self, name):
        self.name = name
        self.instructors = list()
        self.students = list()

    def add_students(self, *students):
        self.students.extend(students)

    def add_instructors(self, *cohort_instructors):
        self.instructors.extend(cohort_instructors)
        for instructor in cohort_instructors:
            return f'{instructor.first_name} {instructor.last_name}'
