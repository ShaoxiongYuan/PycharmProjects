-- 创建函数
delimiter $$
create function stu() returns int
begin
    return (select score from class_1 order by score desc limit 1);
end $$
delimiter ;

-- 调用函数
select stu();

select *
from class_1
where score = stu();


-- *************************************************************************
delimiter $$
create function stu1() returns int
begin
    update class_1 set score = 99 where id = 2;
    return (select score from class_1 order by score desc limit 1);
end $$
delimiter ;

select stu1();