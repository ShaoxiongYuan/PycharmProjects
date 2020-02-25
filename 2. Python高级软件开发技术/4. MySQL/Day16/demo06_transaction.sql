begin;

select *
from class_1;
update class_1
set score=60
where id = 2;
delete
from class_1
where name = 'Lily';

commit;

-- ***************************************************************
begin;

delete
from class_1;

rollback;