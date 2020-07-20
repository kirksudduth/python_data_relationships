from nss_person import NSS_person


class Instructor(NSS_person):
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)

    def __str__(self):
        return f'{self.first_name} {self.last_name} is one of the instructors for the {self.cohort}.'
