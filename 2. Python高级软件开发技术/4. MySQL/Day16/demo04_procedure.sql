-- 创建存储过程
delimiter //
create procedure stu()
begin
    select name, age from class_1;
    select name, score from class_1 order by score desc;
end //
delimiter ;

call stu();

-- procedure形参
-- in
delimiter $$
create procedure p_in(in num int)
begin
    select num;
    set num = 100;
    select num;
end $$
delimiter ;

call p_in(10);

-- out
delimiter $$
create procedure p_out(out num int)
begin
    select num;
    set num = 100;
    select num;
end $$
delimiter ;

set @num = 10;
call p_out(@num);

-- inout
delimiter $$
create procedure p_inout(inout num int)
begin
    select num;
    set num = 100;
    select num;
end $$
delimiter ;

set @num = 10;
call p_inout(@num);