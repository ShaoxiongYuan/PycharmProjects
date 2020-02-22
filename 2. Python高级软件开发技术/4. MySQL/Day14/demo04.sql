-- 聚合
select max(attack)
from sanguo;

select avg(attack)
from sanguo;

select sum(attack)
from sanguo;

select min(attack)
from sanguo;

select count(name)
from sanguo;

select count(*)
from sanguo
where country = '蜀';

select gender, count(*)
from sanguo
group by gender;

select country, avg(attack)
from sanguo
group by country;

select country, gender, count(*)
from sanguo
group by country, gender;

select country, count(*) as number
from sanguo
where gender = '男'
group by country
order by number desc
limit 2;