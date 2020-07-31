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





CREATE TABLE exercises
(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    language TEXT NOT NULL
);

CREATE TABLE cohorts
(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE students
(
    id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY
(cohort_id) REFERENCES cohorts
(id)
);

CREATE TABLE instructors
(
    id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    specialty TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY
(cohort_id) REFERENCES cohorts
(id)
);

CREATE TABLE students_exercises
(
    id INTEGER NOT NULL PRIMARY KEY,
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

INSERT INTO exercises
VALUES
    (null, "The Big Trip", "Python");
INSERT INTO exercises
VALUES
    (null, "Gallons of What?!", "CSS");
INSERT INTO exercises
VALUES
    (null, "Caring is Sharing", "JavaScript");
INSERT INTO exercises
VALUES
    (null, "Data, My Love", "SQL");
INSERT INTO exercises
VALUES
    (null, "Hooks for the Ages", "JavaScript");


INSERT INTO instructors
VALUES
    (null, "Joe", "Shepherd", "joes", "mixing petrol and teaching the code", 1);
INSERT INTO instructors
VALUES
    (null, "Bryan", "Nilsen", "bryguy", "dunking basketballs and rocking out", 2);
INSERT INTO instructors
VALUES
    (null, "Madi", "Peper", "mpeper", "dominating dad jokes", 3);

INSERT INTO students
VALUES
    (null, "Michael", "Jordan", "hisairness", 1);
INSERT INTO students
VALUES
    (null, "Steve", "Kerr", "stevekerr", 2);
INSERT INTO students
VALUES
    (null, "Scottie", "Pippen", "big33", 1);
INSERT INTO students
VALUES
    (null, "Dennis", "Rodman", "hustle&glow", 3);
INSERT INTO students
VALUES
    (null, "Luc", "Longley", "liluc", 3);
INSERT INTO students
VALUES
    (null, "Toni", "Kukoc", "tk7", 1);
INSERT INTO students
VALUES
    (null, "Horace", "Grant", "mrspecs", 2);

INSERT INTO students_exercises
VALUES
    (null, 1, 5);
INSERT INTO students_exercises
VALUES
    (null, 1, 3);
INSERT INTO students_exercises
VALUES
    (null, 2, 1);
INSERT INTO students_exercises
VALUES
    (null, 2, 2);
INSERT INTO students_exercises
VALUES
    (null, 3, 4);
INSERT INTO students_exercises
VALUES
    (null, 3, 5);
INSERT INTO students_exercises
VALUES
    (null, 4, 1);
INSERT INTO students_exercises
VALUES
    (null, 4, 4);
INSERT INTO students_exercises
VALUES
    (null, 5, 2);
INSERT INTO students_exercises
VALUES
    (null, 5, 3);
INSERT INTO students_exercises
VALUES
    (null, 6, 5);
INSERT INTO students_exercises
VALUES
    (null, 6, 4);
INSERT INTO students_exercises
VALUES
    (null, 7, 3);
INSERT INTO students_exercises
VALUES
    (null, 7, 1);

SELECT e.id ExerciseId,
    e.name,
    s.id,
    s.first_name,
    s.last_name
FROM exercises e
    JOIN students_exercises se on se.exercise_Id = e.Id
    JOIN Students s ON s.id = se.Student_id
ORDER BY e.id;


