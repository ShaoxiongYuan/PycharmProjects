update book
set price=45
where name = '呐喊';

alter table book
    add publish_date date after price;

update book
set publish_date='2016-10-1'
where author = '老舍';

update book
set publish_date='2018-1-1'
where publisher = '人民文学出版社'
  and author != '老舍';

delete
from book
where price > 60;

alter table book
    modify price decimal(5, 2);

select *
from book
where publish_date > '2017-1-1'
  and author = '鲁迅';

