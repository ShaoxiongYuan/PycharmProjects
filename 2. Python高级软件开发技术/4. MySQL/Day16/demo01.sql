-- 多表查询
select person.name, dept.dname
from person,
     dept
where person.dept_id = dept.id;

-- inner join
select *
from person
         inner join dept on person.dept_id = dept.id;

select *
from person
         inner join dept on person.dept_id = dept.id
where salary > 20000;


-- left join
select *
from person
         left join dept on person.dept_id = dept.id;

-- right join
select *
from person
         right join dept on person.dept_id = dept.id;