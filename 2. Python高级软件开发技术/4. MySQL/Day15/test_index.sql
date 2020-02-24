select *
from index_test
where name = 'Tom1234567';
-- 时间：1s 595ms

create unique index name on index_test (name);

-- 有index之后...
select *
from index_test
where name = 'Tom1234567';
-- 时间：74ms