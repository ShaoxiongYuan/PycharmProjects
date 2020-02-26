create table student
(
    s_id   varchar(10) primary key,
    s_name varchar(20),
    s_age  date,
    s_sex  varchar(10)
);

create table teacher
(
    t_id   varchar(10) primary key,
    t_name varchar(20)
);

create table course
(
    c_id   varchar(10) primary key,
    c_name varchar(20),
    t_id   varchar(10)
);

create table score
(
    s_id  varchar(10),
    c_id  varchar(10),
    score varchar(10),
    primary key (s_id, c_id)
);

insert into student (s_id, s_name, s_age, s_sex)
values ('01', '赵雷', '1990-01-01', '男'),
       ('02', '钱电', '1990-12-21', '男'),
       ('03', '孙风', '1990-05-20', '男'),
       ('04', '李云', '1990-08-06', '男'),
       ('05', '周梅', '1991-12-01', '女'),
       ('06', '吴兰', '1992-03-01', '女'),
       ('07', '郑竹', '1989-07-01', '女'),
       ('08', '王菊', '1990-01-20', '女');

insert into course
values ('01', '语文', '02'),
       ('02', '数学', '01'),
       ('03', '英语', '03');

insert into teacher (t_id, t_name)
values ('01', '张三'),
       ('02', '李四'),
       ('03', '王五');

insert into score (s_id, c_id, score)
values ('01', '01', 80),
       ('01', '02', 90),
       ('01', '03', 99),
       ('02', '01', 70),
       ('02', '02', 60),
       ('02', '03', 80),
       ('03', '01', 80),
       ('03', '02', 80),
       ('03', '03', 80),
       ('04', '01', 50),
       ('04', '02', 30),
       ('04', '03', 20),
       ('05', '01', 76),
       ('05', '02', 87),
       ('06', '01', 31),
       ('06', '03', 34),
       ('07', '02', 89),
       ('07', '03', 98);


create table total(
    select a.s_id   as s_id,
           a.s_name as s_name,
           a.s_age  as s_age,
           a.s_sex  as s_sex,
           b.c_id   as c_id,
           b.score  as score,
           c.t_id   as t_id,
           d.t_name as t_name
    from student a
             left join
         score b on a.s_id = b.s_id
             left join
         course c on b.c_id = c.c_id
             left join
         teacher d on c.t_id = d.t_id
);