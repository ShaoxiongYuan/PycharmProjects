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

-- *************************************************************************
-- 有参数
delimiter //
create function queryNameById(uid int) returns varchar(30)
begin
    return (select name from class_1 where id = uid);
end //
delimiter ;

select queryNameById(3) as name;

-- 有变量
delimiter //
create function stu2() returns int
begin
    declare a int;
    declare b int;
    set a = (select score from class_1 where name = 'Amy');
    select score from class_1 where name = 'Lily' into b;
    return a - b;
end //
delimiter ;

select stu2();

delimiter //
create function scoreDifById(uid1 int, uid2 int) returns int
begin
    declare a int;
    declare b int;
    set a = (select score from class_1 where name = queryNameById(uid1));
    set b = (select score from class_1 where name = queryNameById(uid2));
    return a - b;
end //
delimiter ;

select scoreDifById(4, 3);