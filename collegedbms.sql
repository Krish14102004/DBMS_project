create table department
(
    dept_id   int auto_increment
        primary key,
    dept_name varchar(50) not null
);

create table faculty
(
    F_id            int auto_increment
        primary key,
    Faculty_name    varchar(50) not null,
    F_dept          varchar(50) null,
    Salary          int         null,
    Faculty_Phoneno varchar(15) null,
    dept_id         int         null,
    constraint fk_faculty_dept
        foreign key (dept_id) references department (dept_id)
);

create table course
(
    course_id   int auto_increment
        primary key,
    course_name varchar(50) not null,
    Duration    int         null,
    F_id        int         null,
    constraint fk_course_faculty
        foreign key (F_id) references faculty (F_id)
);

create table hostel
(
    hostel_id   int auto_increment
        primary key,
    hostel_name varchar(50) not null,
    no_of_seats int         null
);

create table student
(
    S_id      int auto_increment
        primary key,
    S_name    varchar(50)  not null,
    Age       int          null,
    dob       date         null,
    p_no      varchar(15)  null,
    S_Address varchar(100) null,
    FA_id     int          null,
    dept_id   int          null,
    hostel_id int          null,
    constraint fk_student_dept
        foreign key (dept_id) references department (dept_id),
    constraint fk_student_hostel
        foreign key (hostel_id) references hostel (hostel_id),
    constraint fk_student_faculty_advisor
        foreign key (FA_id) references faculty (F_id)
);

create table subject
(
    Sub_id    int auto_increment
        primary key,
    Sub_name  varchar(50) not null,
    course_id int         null,
    constraint fk_subject_course
        foreign key (course_id) references course (course_id)
);

create table exam
(
    Exam_code    int auto_increment
        primary key,
    Room_no      varchar(50) not null,
    Exam_timings datetime    null,
    Sub_id       int         null,
    constraint fk_exam_subject
        foreign key (Sub_id) references subject (Sub_id)
);

create definer = root@localhost view coursesubjects as
select `c`.`course_id`                             AS `course_id`,
       `c`.`course_name`                           AS `course_name`,
       `c`.`Duration`                              AS `Duration`,
       group_concat(`s`.`Sub_name` separator ', ') AS `Subjects`
from (`universitymanagementsystem`.`course` `c` left join `universitymanagementsystem`.`subject` `s`
      on ((`c`.`course_id` = `s`.`course_id`)))
group by `c`.`course_id`, `c`.`course_name`, `c`.`Duration`;

create definer = root@localhost view examschedule as
select `e`.`Exam_code`    AS `Exam_code`,
       `e`.`Room_no`      AS `Room_no`,
       `e`.`Exam_timings` AS `Exam_timings`,
       `s`.`Sub_name`     AS `Sub_name`
from (`universitymanagementsystem`.`exam` `e` left join `universitymanagementsystem`.`subject` `s`
      on ((`e`.`Sub_id` = `s`.`Sub_id`)));

create definer = root@localhost view facultyinfo as
select `f`.`F_id`         AS `F_id`,
       `f`.`Faculty_name` AS `Faculty_name`,
       `f`.`F_dept`       AS `F_dept`,
       `f`.`Salary`       AS `Salary`,
       `d`.`dept_name`    AS `Department`
from (`universitymanagementsystem`.`faculty` `f` left join `universitymanagementsystem`.`department` `d`
      on ((`f`.`dept_id` = `d`.`dept_id`)));

create definer = root@localhost view hosteloccupancy as
select `h`.`hostel_id`        AS `hostel_id`,
       `h`.`hostel_name`      AS `hostel_name`,
       `h`.`no_of_seats`      AS `no_of_seats`,
       count(`s`.`hostel_id`) AS `Current_Occupancy`
from (`universitymanagementsystem`.`hostel` `h` left join `universitymanagementsystem`.`student` `s`
      on ((`h`.`hostel_id` = `s`.`hostel_id`)))
group by `h`.`hostel_id`, `h`.`hostel_name`, `h`.`no_of_seats`;

create definer = root@localhost view studentinfo as
select `s`.`S_id`         AS `S_id`,
       `s`.`S_name`       AS `S_name`,
       `s`.`Age`          AS `Age`,
       `s`.`dob`          AS `dob`,
       `s`.`p_no`         AS `p_no`,
       `s`.`S_Address`    AS `S_Address`,
       `f`.`Faculty_name` AS `Advisor`,
       `d`.`dept_name`    AS `Department`,
       `h`.`hostel_name`  AS `Hostel`
from (((`universitymanagementsystem`.`student` `s` left join `universitymanagementsystem`.`faculty` `f`
        on ((`s`.`FA_id` = `f`.`F_id`))) left join `universitymanagementsystem`.`department` `d`
       on ((`s`.`dept_id` = `d`.`dept_id`))) left join `universitymanagementsystem`.`hostel` `h`
      on ((`s`.`hostel_id` = `h`.`hostel_id`)));

