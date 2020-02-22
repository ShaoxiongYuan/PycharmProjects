-- 查询
select *
from student.class_1
where age % 2 = 0;

select *
from student.class_1
where sex is not null;

use student;
select *
from class_1
where score > 90
   or score < 60;

select *
from class_1
where score >= 80 xor sex = 'm';

-- 更新
update class_1
set age=14
where name = 'Lily';

update class_1
set age=age + 1
where name = 'Baron';

update class_1
set age=25
where age = 14;

-- 删除
delete
from class_1
where name = 'Baron';

-- alter
alter table interest
    add tel char(11) after price;

alter table interest
    drop price;

alter table interest
    modify tel char(16);

alter table interest
    change tel telephone char(11);

alter table class_1 rename cls;
-- rename table class_1 to cls;
