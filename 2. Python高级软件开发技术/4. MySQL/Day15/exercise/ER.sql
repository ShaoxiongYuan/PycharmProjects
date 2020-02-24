create table student
(
    id         int primary key auto_increment,
    name       varchar(20)      not null,
    age        tinyint unsigned not null,
    sex        enum ('w','m','o') default 'o',
    born_place varchar(20)
);

create table teacher
(
    id    int primary key auto_increment,
    name  varchar(20)      not null,
    place varchar(20),
    age   tinyint unsigned not null
);

create table lesson
(
    id          int primary key auto_increment,
    name        varchar(50) not null,
    grade_point int default 0,
    teacher_id  int         not null,
    constraint tid_fk foreign key (teacher_id) references teacher (id)
);

create table student_lesson
(
    student_id int     not null,
    lesson_id  int     not null,
    grade      char(2) not null,
    primary key (student_id, lesson_id),
    constraint sid_fk foreign key (student_id) references student (id),
    constraint lid_fk foreign key (lesson_id) references lesson (id)
);