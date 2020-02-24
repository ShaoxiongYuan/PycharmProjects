-- having
select country, avg(attack)
from sanguo
group by country
having avg(attack) > 250
order by avg(attack) desc
limit 2;

select country, avg(defense)
from sanguo
where gender = '男'
group by country
having avg(defense) > 65.7;

-- distinct
select count(distinct country)
from sanguo;

select distinct country
from sanguo;

-- 运算
update sanguo
set attack=attack * 2
where country = '吴'
  and gender = '男';

select name, attack * 2
from sanguo;