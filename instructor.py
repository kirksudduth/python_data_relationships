
class Instructor:
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)

    def __str__(self):
        return f'{self.first_name} {self.last_name} is one of the instructors for the {self.cohort}.'
