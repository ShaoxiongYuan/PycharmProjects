select author, avg(price)
from book
group by author;

select publisher, count(name)
from book
group by publisher;

select count(distinct publisher)
from book;

select publisher, max(price)
from book
group by publisher
having max(price) > 50
order by max(price) desc;

select publish_date, avg(price)
from book
group by publish_date;


