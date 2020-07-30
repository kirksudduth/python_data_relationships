DELETE FROM exercises;
DELETE FROM cohorts;
DELETE FROM students;
DELETE FROM instructors;
-- DELETE FROM students_exercises;

DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS instructors;
-- DROP TABLE IF EXISTS students_exercises;





CREATE TABLE exercises (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    language TEXT NOT NULL
);

CREATE TABLE cohorts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE students (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY
(cohort_id) REFERENCES cohorts
(id)
);

CREATE TABLE instructors (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    specialty TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY
(cohort_id) REFERENCES cohorts
(id)
);

CREATE TABLE students_exercises (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    FOREIGN KEY
(student_id) REFERENCES students
(id),
    FOREIGN KEY
(exercise_id) REFERENCES exercises
(id)
);

INSERT INTO cohorts
VALUES
    (null, "Day Cohort 40");
INSERT INTO cohorts
VALUES
    (null, "Evening Cohort 23");
INSERT INTO cohorts
VALUES
    (null, "Night Cohort 15");


