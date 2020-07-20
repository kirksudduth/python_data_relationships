
class NSS_person:
    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')
