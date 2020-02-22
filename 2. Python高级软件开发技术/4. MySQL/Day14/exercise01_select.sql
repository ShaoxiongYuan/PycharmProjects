-- 练习2 查找练习
--
-- 1. 查找30多图书
-- 2. 查找中国教育出版社出版的图书
-- 3. 查找老舍写的，中国文学出版社出版的
-- 4. 查找备注不为空的
-- 5. 查找价格超过60的，只看书名和价格
-- 6. 查找鲁迅写的 或者 矛盾写的
use books;

-- 1.
select *
from book
where price >= 30
  and price < 40;

-- 2.
select *
from book
where publisher = '中国教育出版社';

-- 3.
select *
from book
where author = '老舍'
  and publisher = '中国文学出版社';

-- 4.
select *
from book
where note is not null;

-- 5.
select name, price
from book
where price > 60;

-- 6.
select *
from book
where author in ('鲁迅', '矛盾')