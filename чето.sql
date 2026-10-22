CREATE SCHEMA Academy;
USE Academy;

CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE student_group (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES classes(id)
);

CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE student_grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES student_group(id)
);

CREATE TABLE lessons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject_id INT,
    teacher_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lesson_id INT,
    group_id INT,
    schedule_date DATETIME,
    FOREIGN KEY (lesson_id) REFERENCES lessons(id),
    FOREIGN KEY (group_id) REFERENCES student_group(id)
);
