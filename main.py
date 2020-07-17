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
wolfgang_amadeus.assign_exercise(tim_hill, critter_crunch, planetary_pause)
wolfgang_amadeus.assign_exercise(tina_hyman, style_saavy, planetary_pause)
wolfgang_amadeus.assign_exercise(
    terri_howard, egregiously_excited, lousy_loungers)
wolfgang_amadeus.assign_exercise(
    theodore_hankins, critter_crunch, lousy_loungers)

johann_sebastian.assign_exercise(tim_hill, style_saavy, planetary_pause)
johann_sebastian.assign_exercise(
    tina_hyman, egregiously_excited, lousy_loungers)
johann_sebastian.assign_exercise(terri_howard, critter_crunch, lousy_loungers)
johann_sebastian.assign_exercise(
    theodore_hankins, planetary_pause, egregiously_excited)

ludwig_beethoven.assign_exercise(
    tina_hyman, egregiously_excited, planetary_pause)
ludwig_beethoven.assign_exercise(terri_howard, critter_crunch, lousy_loungers)
ludwig_beethoven.assign_exercise(
    theodore_hankins, egregiously_excited, critter_crunch)
ludwig_beethoven.assign_exercise(
    tim_hill, egregiously_excited, planetary_pause)


def Strings(exercises):
    def __str__(self, exercises):
        for exercise in exercises:
            return f'{exercise.name} is an exercise using {exercise.language}'


print(Strings(t_h_exercises))
