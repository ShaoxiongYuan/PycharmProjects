-- 创建视图
create view good_student as
select id, name, sex, score
from class_1
where score > 85;

insert into good_student
values (9, 'Danny', 'm', 86);

-- 删除视图
drop view good_student;

