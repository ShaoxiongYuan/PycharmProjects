use student;

-- 时间数据类型
create table marathon
(
    id                int primary key auto_increment,
    athlete           varchar(32),
    birthday          date,
    registration_time datetime,
    performance       time
);
insert into marathon
values (1, '曹操', '1990-3-3', '2020-1-5 12:12:12', '2:10:13');

insert into marathon (athlete, birthday, registration_time, performance)
VALUES ('关羽', '1991-7-8', '2011-3-5 17:35:59', '2:05:1');

insert into marathon (athlete, birthday, registration_time, performance)
VALUES ('张飞', '1993-10-19', '2018-9-12 19:46:28', '2:15:56');

-- 查找
select *
from marathon
where registration_time < now();

select *
from marathon
where birthday > '1991-3-3';