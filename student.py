
class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.exercises = list()

    def __str__(self):
        return f'{self.first_name} {self.last_name} is a student at NSS attending {self.cohort}.'
