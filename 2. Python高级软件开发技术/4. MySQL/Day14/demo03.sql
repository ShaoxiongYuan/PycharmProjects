-- 模糊查询
select *
from class_1
where name like 'T%';

select *
from class_1
where name like '____';

select *
from class_1
where name regexp '^T.+';

select *
from class_1
where name regexp 'y$';

-- as
select name as n, age as a
from class_1 as c
where c.name = 'Tony';

-- 排序
select *
from class_1
order by score;

select *
from class_1
where sex = 'w'
order by score;

select *
from class_1
order by age, score;

-- limit
select *
from class_1
where sex = 'm'
order by score desc
limit 1;

select *
from class_1
order by score desc
limit 3;

update class_1
set score=96
where sex = 'w'
limit 1;

-- union
select *
from class_1
where sex = 'w'
union
select *
from class_1
where score < 90;

select name, age, sex
from class_1
where sex = 'w'
union
select name, hobby, price
from interest
where price > 3000;

-- 子查询
select name, score
from (select * from class_1 where sex = 'w') as s
where s.score > 90;

select *
from class_1
where score < (select score from class_1 where name = 'Lily');