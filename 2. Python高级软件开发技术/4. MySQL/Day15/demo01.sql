-- having
select country, avg(attack)
from sanguo
group by country
having avg(attack) > 105
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
