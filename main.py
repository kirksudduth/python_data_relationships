from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

tim_hill = Student("Tim", "Hill", "timmyBoi28", "Day Cohort 44")
tina_hyman = Student("Tina", "Hyman", "tina_hyman", "Evening Cohort 29")
terri_howard = Student("Terri", "Howard", "howard_terry", "Day Cohort 43")
theodore_hankins = Student("Theodore", "Hankins",
                           "the_hankins", "Evening Cohort 28")

critter_crunch = Exercise("Critter Time", "Python")
planetary_pause = Exercise("Planetary Pause", "JavaScript")
egregiously_excited = Exercise("Egregiously Excited", "C#")
lousy_loungers = Exercise("Lousy Loungers", "HTML")
style_saavy = Exercise("Style Saavy", "CSS")

day_44 = Cohort("Day Cohort 44")
evening_28 = Cohort("Evening Cohort 28")
day_43 = Cohort("Day Cohort 43")
evening_29 = Cohort("Evening Cohort 29")

wolfgang_amadeus = Instructor(
    "Wolfgang", "Mozart", "wolf_composes", "Day Cohort 44", "being a virtuoso")
johann_sebastian = Instructor(
    "Johann", "Bach", "joseba", "Day Cohort 44", "being one of the greats")
ludwig_beethoven = Instructor(
    "Ludwig", "Beethoven", "lud_von_bee", "Day Cohort 44", "deaf and deft")

day_44.add_instructors(wolfgang_amadeus, johann_sebastian, ludwig_beethoven)
wolfgang_amadeus.assign_exercise(tim_hill, planetary_pause)
wolfgang_amadeus.assign_exercise(tina_hyman, planetary_pause)
wolfgang_amadeus.assign_exercise(
    terri_howard, lousy_loungers)
wolfgang_amadeus.assign_exercise(
    theodore_hankins, critter_crunch)

johann_sebastian.assign_exercise(tim_hill, style_saavy)
johann_sebastian.assign_exercise(
    tina_hyman, lousy_loungers)
johann_sebastian.assign_exercise(terri_howard, lousy_loungers)
johann_sebastian.assign_exercise(
    theodore_hankins, planetary_pause)

ludwig_beethoven.assign_exercise(
    tina_hyman, egregiously_excited)
ludwig_beethoven.assign_exercise(terri_howard, critter_crunch)
ludwig_beethoven.assign_exercise(
    theodore_hankins, egregiously_excited)
ludwig_beethoven.assign_exercise(
    tim_hill, egregiously_excited)

for exercise in tim_hill.exercises:
    print(f'{exercise.name} is gonna be a fun adventure in {exercise.language}')

students = list()
exercises = list()
students = [tim_hill, tina_hyman, terri_howard, theodore_hankins]
exercises = [critter_crunch, planetary_pause,
             egregiously_excited, lousy_loungers, style_saavy]


def exercise_function(exercises):
    return [f'{exercise.name}' for exercise in exercises]


for student in students:
    student_exercises = ", ".join(exercise_function(student.exercises))
    print(f'{student.first_name} {student.last_name} is working on {student_exercises}.')

tim_hill.full_name()
