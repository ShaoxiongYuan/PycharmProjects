show procedure status like 'p_out';

show create function stu;

-- linux查看所有函数/procedure
# select name from mysql.proc where db='student' and type='procedure';

drop function if exists scoreDifById;

drop procedure if exists stu;

