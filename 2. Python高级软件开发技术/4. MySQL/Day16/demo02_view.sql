-- 创建视图
create view good_student as
select id, name, sex, score
from class_1
where score > 85;

insert into good_student
values (9, 'Danny', 'm', 86);


alter view good_student as select c.name, c.sex, c.score, i.hobby
                           from class_1 as c
                                    left join interest as i on c.name = i.name;
-- 删除视图
drop view good_student;

drop view if exists c1;

-- 创建已存在视图并替换
create or replace view good_student as
select id, name, score
from class_1
where score > 95;
