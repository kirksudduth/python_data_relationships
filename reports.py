import sqlite3
from student import Student


# class Student():

#     def __init__(self, first, last, handle, cohort):
#         self.first_name = first
#         self.last_name = last
#         self.slack_handle = handle
#         self.cohort = cohort

#     def __str__(self):
#         return f'{self.first_name} {self.last_name} is in {self.cohort}'


class StudentExerciseReports():

    """Methods for reports on the 
    Student Exercises database """

    def __init__(self):
        self.db_path = "/Users/kirk/workspace/python/student_exercises/student_exercises.db"

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[5])

    def all_students(self):
        """Retrieve all students with 
        the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_student
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.name
            from Students s
            join Cohorts c on s.Cohort_Id = c.Id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(
                    f'{student.first_name} {student.last_name} is in {student.cohort}')


reports = StudentExerciseReports()
reports.all_students()
# student = Student("Bart", "Simpson", "@bart", "Cohort 8")
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')
