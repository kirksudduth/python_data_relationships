from nss_person import NSS_person


class Student(NSS_person):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.exercises = list()

    def __str__(self):
        return f'{self.first_name} {self.last_name} is a student at NSS attending {self.cohort}.'
