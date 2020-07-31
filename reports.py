import sqlite3
from student import Student
from instructor import Instructor
from exercise import Exercise
from cohort import Cohort


class StudentExerciseReports():

    """Methods for reports on the 
    Student Exercises database """

    def __init__(self):
        self.db_path = "/Users/kirk/workspace/python/student_exercises/student_exercises.db"

    def all_students(self):
        """Retrieve all students with 
        the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])
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

            # ***COMPREHENSION _ SUPER CONCISE***
            # does the same thing as for loop
            [print(s) for s in all_students]

    def all_exercises(self):
        """Retrieve all exercises with exercise name"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select ex.id,
                ex.name,
                ex.language
            from exercises ex
            """)
        all_exercises = db_cursor.fetchall()
        # ***COMPREHENSION __ A BETTER FOR LOOP (LESS CHARS)***
        [print(ex) for ex in all_exercises]

    def all_cohorts(self):
        """Retrieve all cohorts with cohort name"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.id,
                c.name
            from cohorts c
            """)

        all_cohorts = db_cursor.fetchall()
        # ***COMPREHENSION __ A BETTER FOR LOOP (LESS CHARS)***
        [print(c) for c in all_cohorts]

    def all_javascript_ex(self):
        """Retrieve all JavaScript exercises"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute(""" 
            select ex.id,
                ex.name,
                ex.language
            from exercises ex 
            where ex.language like "%javas%"
            """)
        all_javascript_ex = db_cursor.fetchall()
        [print(ex) for ex in all_javascript_ex]

    def all_python_ex(self):
        """Retrive all Python exercises"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select ex.id,
                ex.name,
                ex.language
            from exercises ex
            where ex.language like "%python%"
            """)
        all_python_ex = db_cursor.fetchall()
        [print(ex) for ex in all_python_ex]

    def all_instructors(self):
        """Retrieve all instructors with
        the cohort name"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5], row[4])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.cohort_id,
                c.name
            from instructors i
            join cohorts c on i.cohort_id = c.id
            order by i.cohort_id
            """)

        all_instructors = db_cursor.fetchall()
        # ***COMPREHENSION __ A BETTER FOR LOOP (LESS CHARS)***
        [print(i) for i in all_instructors]


reports = StudentExerciseReports()
reports.all_students()
reports.all_instructors()
reports.all_cohorts()
reports.all_exercises()
reports.all_javascript_ex()
reports.all_python_ex()
