CREATE TABLE Groups (
    group_id    VARCHAR(10)  NOT NULL,
    group_name  VARCHAR(100) NOT NULL,
    CONSTRAINT pk_groups PRIMARY KEY (group_id),
    CONSTRAINT uq_groups_name UNIQUE (group_name)
);

CREATE TABLE Students (
    student_id    INT          NOT NULL,
    student_name  VARCHAR(100) NOT NULL,
    group_id      VARCHAR(10)  NOT NULL,
    CONSTRAINT pk_students PRIMARY KEY (student_id),
    CONSTRAINT fk_students_group FOREIGN KEY (group_id)
        REFERENCES Groups (group_id)
);

CREATE TABLE Teachers (
    teacher_id    INT          NOT NULL,
    teacher_name  VARCHAR(100) NOT NULL,
    CONSTRAINT pk_teachers PRIMARY KEY (teacher_id)
);

CREATE TABLE Subjects (
    subject_id    INT          NOT NULL,
    subject_name  VARCHAR(100) NOT NULL,
    teacher_id    INT          NOT NULL,
    CONSTRAINT pk_subjects PRIMARY KEY (subject_id),
    CONSTRAINT uq_subjects_name UNIQUE (subject_name),
    CONSTRAINT fk_subjects_teacher FOREIGN KEY (teacher_id)
        REFERENCES Teachers (teacher_id)
);

CREATE TABLE StudentGrades (
    student_id  INT   NOT NULL,
    subject_id  INT   NOT NULL,
    exam_date   DATE  NOT NULL,
    grade       INT   NOT NULL,
    CONSTRAINT pk_student_grades PRIMARY KEY (student_id, subject_id, exam_date),
    CONSTRAINT fk_grades_student FOREIGN KEY (student_id)
        REFERENCES Students (student_id),
    CONSTRAINT fk_grades_subject FOREIGN KEY (subject_id)
        REFERENCES Subjects (subject_id),
    CONSTRAINT chk_grade CHECK (grade BETWEEN 1 AND 5)
);
